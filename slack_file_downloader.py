# coding: utf-8
import os
import json
import requests
from pathlib import Path

def main(export_dir_path):
    # 指定されたエクスポートディレクトリ以下のファイルを再帰的に処理する
    for root, _, files in os.walk(top=export_dir_path):
        for file in files:

            file_path = os.path.join(root, file)

            # 拡張子がJSONの場合
            path, ext = os.path.splitext(file_path)
            if ext == '.json':

                print(f'file_path = {file_path}')

                # Slackエクスポートファイルを開く
                with open(file_path, 'r', encoding='utf-8') as f:
                    # ファイル内のコンテンツを読み込み、改行を削除する
                    content = f.read().replace('\n', '')
                    # SlackエクスポートファイルをJSONとして読み込む
                    slack_exports = json.loads(content)

                    # メッセージに添付されたファイルを処理する
                    for message in slack_exports:
                        if 'files' in message:
                            for file in message['files']:
                                if 'url_private_download' in file:
                                    url = file['url_private_download']
                                    file_id = file['id']
                                    if 'name' in file:
                                        file_name = file_id + '-' + file['name']
                                    else:
                                        file_name = file_id + os.extsep + file['filetype']
                                    
                                    # 保存先ファイルパスを作成する
                                    destination = f'{path}-{file_name}'

                                    # ファイルをダウンロードする
                                    download_file(url, destination)

def download_file(url, destination):
    # ファイルをダウンロードする
    print(f'Downloading file from {url} to {destination}...')
    r = requests.get(url)
    with open(destination, 'wb') as f:
        f.write(r.content)

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Export Slack attached file")
    parser.add_argument("--export-dir", default="export", help="Slack Export Directory")
    args = parser.parse_args()

    # メイン関数を呼び出し、エクスポートディレクトリを指定する
    main(Path(args.export_dir))
