使用網路資源學習python

----------part 01----------
| 編號 | 學習目標 | 狀態/備註 | 遇到問題與解決方案 |
| :---: | :---: | :---: | :--- |
| 01 | 安裝並運用pygame | ✅ | 對python不熟的部分另開一個explain.py去做註解<br>pygame 無法正確安裝<br>解決過程<br>(1) 確認無法安裝原因(ERROR: Failed to build 'pygame' when getting requirements to build wheel)<br>(2) 確認pygame無法在3.14版執行後降版本去3.12 |
| 02 | 定義位置(視窗、人物位置比例) | ✅ | |
| 03 | 設定class+def後達到可以重複使用 | ✅ | |

----------part 02----------
學習目標
遇到問題與解決方案
1. 87行在設定 pygame.KEYDOWN 相關時出現「輸入法干擾」的問題
解決過程
(1) 用 print 確認 esc 按鍵是否生效，確認生效後往其他方向進行確認
(2) 留意到輸入法問題，給予每個 KEYDOWN 和 KEYUP 一個 print 後確認問題為輸入法
(3) 完成後增加限制輸入法



