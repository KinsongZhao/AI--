import time
import traceback

from my_chrome import MyChrome

if __name__ == '__main__':
    myChrome = MyChrome(isheadless=False)
    try:
        myChrome.goto_url("https://www.dianping.com/haikou/ch30")
        # time.sleep(10)
        myChrome.reload_ck()
        # myChrome.collect_list()
        myChrome.collect_detail()
        time.sleep(10)
    except Exception as e:
        traceback.print_exc()
    finally:
        myChrome.closeChrome()
