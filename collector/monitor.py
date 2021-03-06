import json
import os
import time
from multiprocessing import Process
import dbconn as db
# import kkconn
import config as cfg
import modules.collect.dir as dir


# import network as net
# import config


def daemon():
    conf = cfg.get_config(path=dir.config_path)
    channel_spec = conf["channel_spec"]
    html_save_dir = conf["storage"]["html_save_dir"]
    csv_save_dir = conf["storage"]["csv_save_dir"]

    while True:
        work_group_list = db.session.query(db.WorkGroups) \
            .filter(db.WorkGroups.work_state == 'attached').all()

        work_group_table = {}
        for work_group in work_group_list:
            report = {}
            target_csv_line_count = 0
            channels = work_group.channels.split(',')
            for channel in channels:
                try:
                    target_html_save_dir = cfg.get_save_dir(html_save_dir, work_group.id, channel)
                    target_csv_save_dir = cfg.get_save_dir(csv_save_dir, work_group.id, channel)

                    for filename in os.listdir(target_csv_save_dir):
                        if ".csvf" in filename:
                            continue
                        target_file_path = target_csv_save_dir + filename
                        file = open(target_file_path, 'r')
                        csv_line_count = len(file.readlines()) #file.read().count('\n')+1
                        target_csv_line_count += csv_line_count
                        file.close()

                    report[channel] = {
                        "html_file_count": len(os.listdir(target_html_save_dir)),
                        "csv_line_count": target_csv_line_count# len(os.listdir(target_csv_save_dir))
                    }
                    work_group.report = json.dumps(report, ensure_ascii=False)

                    db.session.commit()
                    db.session.flush()
                except Exception as e:
                    print(e)

        time.sleep(3)


    # File Explorer 탐색
    # 카프카 urls > work_group_no > 채널별 url 개수 맵리듀스 poll방식으로.
    # HTML 저장 폴더 > 채널 폴더 > 파일 개수   len(os.listdir(path))
    # 텍스트 추출 폴더 > 채널 폴더 > 파일 개수    len(os.listdir(path))

    # Kafka URL 집계
    # HTML 파일 개수 집계

    # CSV 추출된 텍스트 라인 집계
    # DB 업데이트


if __name__ == '__main__':
    # Daemon Start.
    daemon()
    # daemon_obj = Process(target=daemon, args=())
    # daemon_obj.start()

    # conf = config.get_config()
    # net.start_rpc_server(conf["server"]["worker"]["addr"], conf["server"]["worker"]["port"])
