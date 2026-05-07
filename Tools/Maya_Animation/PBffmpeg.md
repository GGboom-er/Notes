---
tags: [Maya_Animation, Maya_Rigging, tool]
tech_stack: [PySide/PyQt, Python]
---
# 🛠️ PBffmpeg
> **Playblast and encode with ffmpeg for Maya.**

- 📂 [PBffmpeg](file:///Y:/GGbommer/scripts/PBffmpeg)

## 💡 详细说明
# Playblast ffmpeg
Playblast and encode with ffmpeg for Maya.

## 機能
- カスタム設定でPlayblast
- ffmpegでPlayblastをエンコード
- エンコード後にPlayblastファイルを自動的に削除
- エンコード後にファイルとフォルダを開く

## 環境
- Maya 2017以降 (Maya 2025で動作確認済み)
- PySide2またはPySide6
- ffmpeg

## インストール
1. `playblast-ffmpeg.py`を[Releases](https://github.com/Dolphiiiin/playblast-ffmpeg/releases)からダウンロード
2. 公式サイトから`ffmpeg`実行ファイルをダウンロード: https://ffmpeg.org/download.html
3. ダウンロードしたスクリプトと`ffmpeg`実行ファイルをMayaの`scripts`ディレクトリに配置
(日本語版Mayaでは`C:\Users\{UserName}\Documents\maya\{Version}\ja_JP\scripts`に配置します)

## 使い方
1. Mayaのスクリプトエディタで以下のコードを実行:
```python
import playblast_ffmpeg
playblast_ffmpeg.showUI()
```
2. プレイブラストオプションを設定
3. `Export`ボタンをクリックしてビデオをPlayblastしてエンコード

# パラメーター
| 項目 | 説明 |
| --- | --- |
| `装飾の表示` | ビューポートのヘッドアップディスプレイのような装飾をプレイブラストに表示します |
| `ポリゴンのみ表示` | ポリゴンのみを表示して、プレイブラストをエンコードします |
| `精度` | レンダリング精度を設定します |
| `表示サイズ` | プレイブラストのレンダリング解像度を設定します |
| `スケール` | 解像度をスケーリングします |
| `フレームパディング` | フレームパディングを設定します |
| `上書きして保存` | 有効の時、上書きの確認ダイアログ
