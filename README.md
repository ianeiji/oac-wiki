# oac-wiki

Civilization IV: Beyond the Sword のMOD「Fall from Heaven 2（FfH2）」と、そのMODMOD「OAC（Omniscience Almighty Creature）」の攻略資料をまとめた個人用リポジトリ。
主に Claude に質問して答えさせるための資料として使う（回答ルールは `CLAUDE.md`）。

## 出典

- Civ4/FfH2情報局 OAC: http://kentasis.web.fc2.com/OAC/top.htm
- Civ4/FfH2情報局 FfH2: http://kentasis.web.fc2.com/FfH2/top.htm
- OAC 0.57 のゲームファイル（インストール済みの `Assets/XML` と `Assets/python`）

## 構成

| フォルダ | 内容 |
|---|---|
| `oac-057/` | OAC 0.57 のデータ。ゲームのXMLから `tools/` のスクリプトで生成（最優先で参照） |
| `oac-p29/` | OAC 0.56 非公式Patch29 のデータ（情報局のページを変換） |
| `oac-056/` | OAC 0.56 公式開発版のデータ（同上） |
| `oac-notes/` | OAC の解説・考察（同上。考察は執筆時点のバージョン準拠） |
| `ffh2/` | FfH2本家（BtS 0.41o）の解説・考察と、OAC版がないデータ（同上） |
| `patchnotes/` | OAC 0.57 のパッチノート |
| `python/` | OAC 0.57 の Python ソース（呪文・イベントなど、XMLにない効果の実装）。UTF-8に変換済み |
| `tools/` | XML から `oac-057/` を生成するスクリプト |

ファイルごとの内容は `INDEX.md` を参照。

## 補足

- `oac-057/` のデータはXMLを機械的に変換したもの。主要項目以外は XML のタグ名のまま残っている。Pythonで実装された効果は `python/` を、C++（DLL）で実装された仕組みはどこにも含まれない。
- 情報局のデータページ（P29・0.56）は説明が詳しいが、0.57の変更は反映されていない。0.57の変更点は `patchnotes/` と `oac-057/` で確認する。
- OAC を更新したときは、`tools/` のスクリプトで `oac-057/` を作り直せる（使い方は各スクリプト冒頭のコメント）。テキストはMOD側に加えてゲーム本体（BtS と無印）の `Assets/XML/Text` も渡すこと。
