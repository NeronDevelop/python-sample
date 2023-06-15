from datetime import datetime
import os

def makeDirectory(root="./", dirs="", today_mode=False):
    """
    ディレクトリを作成する

    Parameters
    ----------
    root: string
        作成対象のルートディレクトリ
    dir: string
        作成対象のディレクトリ名
    today_mode: boolean
        Trueに指定すると、一番上の階層が"本日の日付"(YYYY-MM-DD)が付与さて作成される    
    """

    import pdb
    pdb.set_trace()
    make_dir = ""
    if today_mode:
        today_str = datetime.now().strftime('%Y-%m-%d')
        make_dir = root + "/" + today_str + "/" + dirs
    else:
        make_dir = root + "/" + dirs

    # ディレクトリが既存のものだったら何もしない
    if os.path.isdir(make_dir):
        return
    os.makedirs(make_dir)

if __name__ == "__main__":
    makeDirectory(today_mode=True)