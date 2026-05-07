---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [C++, MEL, Python]
---
# 🛠️ maya_exprespy
> **Maya で Python によるエクスプレッション機能を提供するノードのプラグインです。**

- 📂 [maya_exprespy](file:///Y:/GGbommer/scripts/maya_exprespy)

## 💡 详细说明
# maya_exprespy
Maya で Python によるエクスプレッション機能を提供するノードのプラグインです。
exprespy（エクスプレスパイ）と呼びます。

![exprespy](images/exprespy.png)



## 特徴
本プラグインは実行速度を重視し、C++ でノードが実装されています。
また、それによって、Pythonエクスプレッションコードはコンパイルされたものがメモリに保持され、
効率的に実行されるようになっています。

また、エディタ（アトリビュートエディタ）上では、標準のエクスプレッション機能と同様に
実際のノード・アトリビュート名でのコーディングが可能です。
それらは、標準機能と同様に、実際はノードのコネクションに置き換えられるようになっています。
ただし、単位変換の機能はなく常に内部単位で扱われるという点が標準機能と異なります。
これだけが少し初心者向けでない部分ですが、効率重視たる所以です。

さらに、Python API 2.0 の型に対応し、double3 や matrix アトリビュートはもちろんのこと、
ジオメトリデータなどあらゆるデータ型を直接入出力することが可能です。

Maya バージョンに応じて Python 2.x と Python 3.x に両対応しています。

[制限事項](#limitation) をご一読の上ご利用ください。



## 類似技術
標準で付属する MASH には Python ノードがあり、Python でモーショングラフィックスを制御することが出来ます。
ただ、それは particle データを制御する仕組みで、それに特化された性能は素晴らしいですが汎用的なものではありません。

また、Python で通常のエクスプレッションを書けるようにするプラグインは
[SOuP](http://www.soup-dev.com/)
に含まれる
[pyExpression](http://www.soup-dev.com/wiki/PyExpression.html)
ノードが有名です。
しかし、それは全て Python で実装されており、
Python のエクスプレッションコードは exec() 関数によって実行される仕組みで、
実行するたびにコードをコンパイルするため効率的で
