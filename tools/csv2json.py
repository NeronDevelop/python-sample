import argparse
import csv
import json


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_path', help='csv file path')
parser.add_argument('-o', '--output_path', help='output file path')
parser.add_argument('--indent', help='if you set this option, indent will be added in output file')
parser.add_argument('--d3', action='store_true', help="if you set this option, d3.js format i.e 'data': [csv contents...]")

args = parser.parse_args()


# TODO: コメントの書き方を学ぶ
#
# sample command.
# python csv2json.py -i "../data/iris.csv" -o "output.json"
#
if __name__ == "__main__":
    # ファイルの読み込み
    with open(args.input_path, 'r') as f:
        d_reader = csv.DictReader(f)
        d_list = [row for row in d_reader]
    
    # d3.jsのオプションの有無
    output_data = None
    if args.d3:
        output_data = {"data": d_list}
    else:
        output_data = d_list
    
    # ファイルの出力
    with open(args.output_path, 'w') as f:
        json.dump({"data": d_list}, f, indent=args.indent, ensure_ascii=False)