# net_bytes
![test](https://github.com/eLu-0912/net_bytes/actions/workflows/test.yml/badge.svg) 
- これはROS2のパッケージである
- システムのネットワークインターフェースにおける送受信バイト数をトピックから出力する
## ノード概要
* network_info
 * システムのネットワークインターフェースにおける送受信バイト数を取得し、1秒ごとにトピックにパブリッシュする

## トピック概要
* トピック名:`network_info`
* メッセージの型:`String`
## 実行方法
- 実行方法
2つの端末で実行
  - 端末1
`ros2 run net_bytes network_info`
  - 端末2
`ros2 run net_bytes listener`
## 動作環境
### 必要なソフトウェア
* python
### テスト環境
* ubuntu 22.04.2 LTS
* ROS2 Humble
## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布及び使用が許可されます
- このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。
  - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Takeru Harashima
