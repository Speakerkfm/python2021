from glob import glob
import pandas as pd
import numpy as np
import re
from datetime import datetime
import timeit
import ciso8601


def prepare_train_set(logs_path: str,
                      session_length: int,
                      window_size: int,
                      max_duration: int):
    list_of_files = glob(logs_path)
    data = {}
    for path in list_of_files:
        user_id = int(re.search('([1-9][0-9]*).csv$', path).group(1))
        last_session_time = datetime.fromordinal(1)
        with open(path, 'r') as fp:
            list_of_sessions = []
            session = []
            first_line = True
            for line in fp:
                if first_line:
                    first_line = False
                    continue

                # Читаем строки из файла, каждую строку разбиваем на части
                list_of_tokens = line.strip().split(',')
                dt = ciso8601.parse_datetime(list_of_tokens[0])
                site_name = list_of_tokens[1]

                if (dt - last_session_time).seconds > max_duration or \
                        len(session) == session_length:
                    # end previous session
                    if len(session) > 0:
                        list_of_sessions.append(session)
                    new_session = []
                    # create new session from old with window size
                    idx = window_size
                    while idx < len(session):
                        new_session.append(session[idx])
                        idx += 1
                    # new session started
                    session = new_session
                    sl = len(new_session)
                    if sl > 0:
                        # check new session is actual
                        last_session_time = new_session[sl - 1][0]
                        if (dt - last_session_time).seconds > max_duration:
                            list_of_sessions.append(session)
                            session = []
                session.append((dt, site_name))
                last_session_time = dt
            # end last session
            list_of_sessions.append(session)
            session = []
        data[user_id] = list_of_sessions
    result = []
    for user_id, user_info in data.items():
        for list_of_sessions in user_info:
            row = []
            for session in list_of_sessions:
                row.append(session[1])
                row.append(session[0])
            while len(row) < 2 * session_length:
                row.append(None)
                row.append(None)
            row.append(user_id)
            result.append(row)
    headers = []
    i = 0
    while i < session_length:
        idx = str(i + 1).zfill(2)
        headers.append('site' + idx)
        headers.append('time' + idx)
        i += 1
    headers.append('user_id')
    return pd.DataFrame(np.array(result), columns=headers)


if __name__ == '__main__':
    t = timeit.Timer(
        'prepare_train_set(logs_path=\'other_user_logs/*.csv\', '
        'session_length=10, window_size=10, max_duration=30 * 60)',
        globals=globals())
    print(t.timeit(number=5) / 5 * 10 ** 3)
    # result == ~12s
