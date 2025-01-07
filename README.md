# net_bytes
![test](https://github.com/eLu-0912/net_bytes/actions/workflows/test.yml/badge.svg)  
- これはROS2のパッケージです
- システムのネットワークインターフェースにおける送受信バイト数をトピックから出力する
## ノード概要
* network_info  
  * システムのネットワークインターフェースにおける送受信バイト数を取得し、1秒ごとにトピックにパブリッシュする

## トピック概要  
* トピック名:`network_info`  
* メッセージの型:`String`  
## 実行方法  
- 実行方法1  
2つの端末で実行  
  - 端末1  
`ros2 run net_bytes network_info`  
  - 端末2  
`ros2 run net_bytes listener`  
- 実行方法2  
launchファイルを使用して1つの端末で実行  
`ros2 launch net_bytes talk_listen.launch.py`  
## 動作環境
### 必要なソフトウェア
* python  
### テスト環境
* ubuntu 22.04.2 LTS
* ROS2 Humble
## ライセンス  
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されます
- このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Takeru Harshima
