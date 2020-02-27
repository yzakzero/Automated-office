import pandas as pd
import webbrowser


#设置文件路径
data = pd.DataFrame(pd.read_excel('/Users/liuyifeng/Desktop/test.xlsx'))


#遍历第'奖状电子版'下的每一列
for url in data['奖状电子版']:
    #设置指定路径浏览器
    link='/Applications/Microsoft Edge Beta.app/Contents/MacOS/Microsoft Edge Beta'
    webbrowser.register('IE', None, webbrowser.BackgroundBrowser(link))
    webbrowser.get('IE').open(url)


