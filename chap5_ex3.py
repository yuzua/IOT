# ライブラリをインポート
import smbus
import time
import sys
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

# 初期設定
CONNECTION_STRING = "XXXXXXXX"
PROTOCOL = IoTHubTransportProvider.MQTT
# 表示する温度を小数点２桁まで表示
MSG_TXT = "{\"temperature\": %.2f}"
bus = smbus.SMBus(1)

# IoT Hubにデータを送信するための関数
def send_confirmation_callback(message, result, user_context):
    print ( "IoT Hub responded to message with status: %s" % (result) )

def iothub_client_init():
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client

# 温度を読み込む関数
def adt7410():
    block = bus.read_i2c_block_data(0x48, 0x00, 2)
    data = (block[0] << 8 | block[1]) >> 3 # 13ビットデータ
    if (data >= 4096): # 温度が負の場合
        data -= 8192
    temp = data * 0.0625
    return temp

# 関数を実行し繰り返す処理
try:
    client = iothub_client_init()
    # 温度を保存するリストの初期化
    value = []
    # インデックス番号の初期化
    index_num = 0
    # 繰り返し処理
    while True:
        # 温度を読み取りリストの末尾に追加
        value.append(adt7410())
        # 温度読み取り初回かどうか
        if index_num == 0:
            # 初回なら温度を Azure ストレージに転送
            msg_txt_formatted = MSG_TXT % (value[index_num])
            message = IoTHubMessage(msg_txt_formatted)
            client.send_event_async(message, send_confirmation_callback, None)
        # １回前測定した温度と同じか否かを判断
        elif value[index_num - 1] != value[index_num]:
            # 違った温度なら温度を Azure ストレージに転送
            msg_txt_formatted = MSG_TXT % (value[index_num])
            message = IoTHubMessage(msg_txt_formatted)
            client.send_event_async(message, send_confirmation_callback, None)
        # １秒停止
        time.sleep(1)
        # インデックス番号をインクリメント
        index_num += 1

except KeyboardInterrupt:
    pass
