# Slack File Downloader

Slack の公式エクスポート機能を使ってエクスポートしたjsonファイルから、添付ファイルをまとめてダウンロードするスクリプトです。  
ダウンロードしたファイルはjsonと同じフォルダに格納されます。  
公式エクスポート機能でダウンロードした場合、OAuth トークンは自動的に作成されるため、別途作成する必要はありません。  

This script downloads attachments together from a json file exported using Slack's official export function.  
The downloaded files are stored in the same folder as the json.  
When downloading using the official export function, an OAuth token is automatically created, so there is no need to create one separately.

## 動作環境

- Python: 3.9.9
- requests: 2.28.1

## 使い方

1. Slackの公式エクスポート機能でダウンロードしたzipファイルを、任意のパスに解凍します
2. 以下の通りスクリプトを実行します

```console
$ python slack_file_downloader.py --export-dir /path/to/export
file_path = /path/to/export/channels.json
file_path = /path/to/export/integration_logs.json
file_path = /path/to/export/users.json
file_path = /path/to/export/general/2020-12-06.json
Downloading file from https://files.slack.com/files-pri/XXXXX-XXXX/download/image.png?t=xoxe-xxxxxxxxx to /path/to/export/general/general/2020-12-06-XXXXX-XXXXX.png...
...
```
