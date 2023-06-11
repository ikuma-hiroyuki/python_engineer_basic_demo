以下のURLからも私とChatGPTのやりとりを確認できます。

https://chat.openai.com/share/ebf53c49-caca-4598-ad6f-aeba6ae086da



# 質問 ①

```
あなたは優秀なソフトウェアエンジニアです。
Python3 エンジニア基礎認定試験の問題をターミナルで表示、回答できるプログラムを作成してください。

制約条件は以下の通りです。
- 問題はJSONファイルに格納されています。
- JSONファイルは複数あり、それぞれのファイルには複数の問題が格納されています。
- まずはじめに複数あるjsonファイルをユーザーに番号で選択させます。
- 不正な入力があった場合は再度入力を受け付けます。
- ユーザーが選択したjsonファイルの問題のidとquestionを順番に表示し、回答を受け付けます。
- 回答が入力されたら正解を判定し、解説を表示、次の問題へ進みます。
- 前の問題との区切りをわかりやすくするためにターミナルの幅いっぱいに"-"を表示します。
- また、最後に正解数と正答率を表示します。
- 選択肢以外の回答が入力されたら、再度回答を受け付けます。
- 最後の問題まで回答したら終了します。

構造:
jsons/
    question1.json
    question2.json

JSON:
[
    {
        "id":1,
        "question": "問題文",
        "choices": [
            {
                "A": "選択肢A",
                "B": "選択肢B",
                "C": "選択肢C",
                "D": "選択肢D"
            }
        ],
        "answer": "正答",
        "explanation": "解説"
    },
    {
        "id":2,
        "question": "問題文",
        "choices": [
            {
                "A": "選択肢A",
                "B": "選択肢B",
                "C": "選択肢C",
                "D": "選択肢D"
            }
        ],
        "answer": "正答",
        "explanation": "解説"
    },
    # ...
]
```



# 回答 ①

以下は、指定された制約条件に基づいてPythonで実装されたプログラムです。

```python
import json
import os

def display_question(question):
    print("Question ID:", question['id'])
    print("Question:", question['question'])
    print("Choices:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)

def display_explanation(question):
    print("Explanation:", question['explanation'])

def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("No JSON files found in the 'jsons' directory.")
        return

    print("Select a JSON file by entering the corresponding number:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    while True:
        try:
            choice = int(input("Enter the number: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("Enter your answer (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("Invalid answer. Please enter A, B, C, or D.")
            else:
                break

        if answer == question['answer']:
            correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect!")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)  # Print dashes to separate questions

    print("Quiz completed!")
    print("Number of correct answers:", correct_answers)
    print("Accuracy:", correct_answers / len(questions) * 100, "%")

if __name__ == '__main__':
    main()

```

このプログラムは、指定されたディレクトリ（`jsons/`）内の複数のJSONファイルから問題を読み込み、ユーザーに問題を表示して回答を受け取ります。各問題に対して、回答が正解かどうかを判定し、解説と共に結果を表示します。最後に、正解数と正答率を表示します。

プログラムを実行すると、`jsons/`ディレクトリ内のJSONファイルのリストが表示されます。ユーザーは番号を入力してJSONファイルを選択します。選択後、各問題が順番に表示され、回答を入力することができます。回答が正しいかどうかを判定し、解説と共に次の問題に進みます。最後の問題まで回答した後、正解数と正答率が表示されます。

なお、このプログラムは指定された制約条件に基づいて作成されていますが、入力のバリデーションやエラーハンドリングの面でさらに改善する余地があります。必要に応じて、それらの機能を追加してプログラムを強化することができます。



## ここでテストします。

main.pyというモジュールを作りChatGPTが生成したコードを貼付け、実行します。

すると、以下のようなエラーになりました。

```
print("-" * os.get_terminal_size().columns)  # Print dashes to separate questions
Traceback (most recent call last):
  File "/Users/h_ikuma/Desktop/python_engineer_basic/main.py", line 66, in <module>
    main()
  File "/Users/h_ikuma/Desktop/python_engineer_basic/main.py", line 58, in main
    print("-" * os.get_terminal_size().columns)  # Print dashes to separate questions
                ^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 25] Inappropriate ioctl for device
```

そこで次のように質問しました。また、ユーザーに対するメッセージが英語なので日本語にしてもらいます。



# 質問 ②

```
print("-" * os.get_terminal_size().columns)  # Print dashes to separate questions
この部分でエラーになります。
Traceback (most recent call last):
  File "/Users/h_ikuma/Desktop/python_engineer_basic/main.py", line 66, in <module>
    main()
  File "/Users/h_ikuma/Desktop/python_engineer_basic/main.py", line 58, in main
    print("-" * os.get_terminal_size().columns)  # Print dashes to separate questions
                ^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 25] Inappropriate ioctl for device

それからユーザーに対するメッセージを日本語にしてください。
```



# 回答 ②

`os.get_terminal_size()`は、ターミナルのサイズを取得するための関数ですが、一部の環境では`OSError: [Errno 25] Inappropriate ioctl for device`というエラーが発生する場合があります。

この問題を回避するために、ターミナルの幅を固定値（例えば80）に設定することができます。以下は修正したコードです。

```py
import json
import os

TERMINAL_WIDTH = 80  # 固定のターミナル幅

def display_question(question):
    print("問題ID:", question['id'])
    print("問題:", question['question'])
    print("選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)

def display_explanation(question):
    print("解説:", question['explanation'])

def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * TERMINAL_WIDTH)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")

if __name__ == '__main__':
    main()

```

この修正により、ターミナルの幅に関するエラーは回避されます。

また、ユーザーに対するメッセージは日本語に変更しました。



## ここでテストします。

よさそうな雰囲気ですが、ユーザーに選択させるjsonファイルの並び順が気に入らないので修正してもらうことにしました。



# 質問 ③

```
1. questions_sample.json
2. questions2.json
3. questions1.json

ユーザーに選択させるときに表示するこの順番を逆にしてください。
```



# 回答 ③

順番を逆にするために、JSONファイルのリストを逆順に表示するように修正します。以下は修正後のコードです。

```py
import json
import os

TERMINAL_WIDTH = 80  # 固定のターミナル幅

def display_question(question):
    print("問題ID:", question['id'])
    print("問題:", question['question'])
    print("選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)

def display_explanation(question):
    print("解説:", question['explanation'])

def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    json_files.reverse()  # リストを逆順にする

    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * TERMINAL_WIDTH)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")

if __name__ == '__main__':
    main()

```

修正後のコードでは、`json_files.reverse()`によってJSONファイルのリストが逆順になります。そのため、ユーザーに選択させる際には逆順で表示されます。



## ここでテストします。

jsonファイルの並び順は希望のものになりました。

また、選択肢にない数字やアルファベットを選択した場合、再度ユーザーに入力させる処理も上手くいっていることも確認しました。

次はユーザーに表示する「問題:」「選択肢:」「解説:」「回答を入力してください (A, B, C, D): 」の前に改行(\n)があった方が見やすいと感じたのでここは手入力で修正しました。

以下は修正後のコードです。

```py
import json
import os

TERMINAL_WIDTH = 80  # 固定のターミナル幅


def display_question(question):
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question):
    print("\n解説:", question['explanation'])


def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    json_files.reverse()  # リストを逆順にする

    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * TERMINAL_WIDTH)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```



## さらに以下のように修正を加えました

各処理の部分にコメントや型ヒントを加えます。

```py
import json
import os

TERMINAL_WIDTH = 80  # 固定のターミナル幅


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    json_files.reverse()  # リストを逆順にする

    # ファイル番号の選択肢を表示
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    # ユーザーの選択を受け付ける
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    # json ファイルを読み込み
    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    # 問題を開始
    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        # 正誤を判定
        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * TERMINAL_WIDTH)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```



## イクマの見解

また、ターミナルの幅が80で固定されているので可変にしたいです。これはChatGPTにコードを生成してもらいます。



# 質問 ④

```py
import json
import os

TERMINAL_WIDTH = 80  # 固定のターミナル幅


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    json_files.reverse()  # リストを逆順にする

    # ファイル番号の選択肢を表示
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    # ユーザーの選択を受け付ける
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    # json ファイルを読み込み
    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    # 問題を開始
    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        # 正誤を判定
        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * TERMINAL_WIDTH)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```

```
以下の部分はターミナルの幅が変わっても対応できるようにしてください。
print("-" * TERMINAL_WIDTH)  # 区切りの線を表示
```



# 回答 ④

ターミナルの幅が変わっても対応できるように、`print("-" * TERMINAL_WIDTH)`の部分を修正します。以下は修正後のコードです。

```py
import json
import os

def get_terminal_width():
    """
    ターミナルの幅を取得する

    :return: ターミナルの幅
    """
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # ターミナル幅が取得できない場合はデフォルト値として 80 を使用
    return width

TERMINAL_WIDTH = get_terminal_width()  # ターミナルの幅

# 省略...

def main():
    # 省略...

    # 問題を開始
    correct_answers = 0

    for question in questions:
        # 省略...

        display_explanation(question)
        print("-" * TERMINAL_WIDTH)  # ターミナルの幅に合わせて区切りの線を表示

    # 省略...

if __name__ == '__main__':
    main()

```



## イクマの見解

上のような回答を得ましたが、冗長です。

```py
os.get_terminal_size().columns
```

これだけで充分です。



## この回答を受けて以下のように修正しました。

`TERMINAL_WIDTH`を削除し `print("-" * os.get_terminal_size().columns)` に修正。

```py
import json
import os


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def main():
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    json_files.reverse()  # リストを逆順にする

    # ファイル番号の選択肢を表示
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    # ユーザーの選択を受け付ける
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    # json ファイルを読み込み
    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    # 問題を開始
    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        # 正誤を判定
        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```



さらに、以下のjsonファイルのリストを作る部分にもコメントを入れます。

```py
    # json ファイルのリストを作る
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return
```



次はコメントを加えた部分を関数に分割するリファクタリングを行ってもらいます。



# 質問 ⑤

```py
import json
import os


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def main():
    # json ファイルのリストを作る
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return

    json_files.reverse()  # リストを逆順にする

    # ファイル番号の選択肢を表示
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    # ユーザーの選択を受け付ける
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")

    # json ファイルを読み込み
    selected_file = json_files[choice - 1]
    with open(os.path.join('jsons', selected_file)) as f:
        questions = json.load(f)

    # 問題を開始
    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        # 正誤を判定
        if answer == question['answer']:
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)  # 区切りの線を表示

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```

```
上記コードの以下の部分を関数に分割するリファクタリングを行ってください。
# json ファイルのリストを作る
# ファイル番号の選択肢を表示
# ユーザーの選択を受け付ける
# json ファイルを読み込み
# 問題を開始
# 正誤を判定
```



# 回答 ⑤

以下は、指定された部分を関数に分割するようにリファクタリングしたコードです。

```py
import json
import os


def get_json_file_list():
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files):
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file):
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def check_answer(question, answer):
    """
    回答の正誤を判定する

    :param question: 問題の辞書
    :param answer: ユーザーの回答
    :return: 正解ならTrue、不正解ならFalse
    """
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        if check_answer(question, answer):
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```

修正後のコードでは、`get_json_file_list()`関数でJSONファイルのリストを取得し、`display_file_options()`関数で選択肢を表示します。`get_user_choice()`関数はユーザーの選択を受け付け、選択されたJSONファイルのパスを返します。`load_questions()`関数は選択されたJSONファイルから問題を読み込みます。また、`check_answer()`関数では回答の正誤を判定します。これにより、`main()`関数内のコードがより簡潔になり、各機能が関数として分かれることで可読性と保守性が向上します。



## 得られたコードをテストします。

テストしたら `display_question()` と `display_explanation()` が漏れており、エラーになりました、ChatGPTから得られたコードにこの2つの関数を加えました。



さらに、以下の部分も関数に分割してほしいです。

```py
# 問題を表示して回答を受け付ける
    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        if check_answer(question, answer):
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)
```



# 質問 ⑥

```py
import json
import os


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def get_json_file_list():
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files):
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file):
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def check_answer(question, answer):
    """
    回答の正誤を判定する

    :param question: 問題の辞書
    :param answer: ユーザーの回答
    :return: 正解ならTrue、不正解ならFalse
    """
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        display_question(question)

        while True:
            answer = input("\n回答を入力してください (A, B, C, D): ").upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
            else:
                break

        if check_answer(question, answer):
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```

```
# 問題を表示して回答を受け付ける

と言う部分を関数に分割するリファクタリングを行ってください。
```



# 回答 ⑥

以下は、指定された部分を関数に分割するようにリファクタリングしたコードです。

```python
import json
import os


def get_user_answer():
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question):
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return check_answer(question, answer)


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```

修正後のコードでは、`get_user_answer()`関数を追加してユーザーの回答を受け付けます。`present_question()`関数では問題を表示し、`get_user_answer()`を使用して回答を受け付けます。また、回答が正解かどうかを返します。これにより、`main()`関数内のコードが簡潔化され、可読性と保守性が向上します。



## 納品されたコードの検収

どうやらコードの一部が省略されているので全体を表示してもらいます。



# 質問 ⑦

コードが一部省略されているので全体を表示してください。



# 回答 ⑦

おっしゃる通り、前回の回答で一部のコードが省略されてしまっていました。以下に修正後の全体のコードを表示します。

```py
import json
import os


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def get_json_file_list():
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files):
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file):
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def check_answer(question, answer):
    """
    回答の正誤を判定する

    :param question: 問題の辞書
    :param answer: ユーザーの回答
    :return: 正解ならTrue、不正解ならFalse
    """
    return answer == question['answer']


def get_user_answer():
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question):
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return check_answer(question, answer)


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```

お手数をおかけしましたが、これで全体のコードが正しく表示されているはずです。



## ここでテストします。

よさそうな雰囲気です。

各処理を関数に切り分けたため、コード全体の見通しがよくなりました。こうすることでメンテナンス性が向上し、プログラムの品質が上がります。



## イクマの見解

### 冗長な関数を修正 ①

しかし、よく見ると以下の部分は冗長だと感じました。

```py
def check_answer(question, answer):
    """
    回答の正誤を判定する

    :param question: 問題の辞書
    :param answer: ユーザーの回答
    :return: 正解ならTrue、不正解ならFalse
    """
    return answer == question['answer']
```

この `check_answer()` は `present_question()` からしか呼ばれない関数です。

```py
def present_question(question):
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return check_answer(question, answer)
```



そのため、以下のように修正しました。

```py
def present_question():
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']
```



### 冗長な関数の修正 ②

また、`display_explanation()`も冗長だと感じましたので、修正します。



### 型ヒントの追加

次に型ヒントを各関数に加えました。コード全体は以下のようになります。

```py
import json
import os


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def display_explanation(question: dict):
    """
    解説を表示

    :param question: 問題の辞書
    """
    print("\n解説:", question['explanation'])


def get_json_file_list() -> list:
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files: list[str]):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files: list[str]) -> str:
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file: str) -> list[dict]:
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def get_user_answer() -> str:
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question: dict) -> bool:
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print("正解です！")
        else:
            print("不正解です！")
        display_explanation(question)
        print("-" * os.get_terminal_size().columns)

    print("クイズが終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```



### 演習問題時のメッセージの修正

よく見ると全ての回答が終わったあとに「クイズが終了しました！」と表示されるので「模擬試験が終了しました！」に修正します。

その次は「正解です」「不正解です」に色を付けてもらいます。



# 質問 ⑧

次は「正解」の文字列を緑色に、「不正解」の文字列を赤色にしてください。 



# 回答 ⑧

以下のコードを追加することで、「正解」の文字列を緑色に、「不正解」の文字列を赤色に表示できます。

```py
# カラーリセット
RESET = "\033[0m"
# 緑色のテキスト
GREEN = "\033[32m"
# 赤色のテキスト
RED = "\033[31m"

def present_question(question: dict) -> bool:
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']

def main():
    # ...

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print(f"{GREEN}正解です！{RESET}")
        else:
            print(f"{RED}不正解です！{RESET}")
        print("\n解説:", question['explanation'])
        print("-" * os.get_terminal_size().columns)

    # ...

```

これにより、正解が緑色で表示され、不正解が赤色で表示されます。緑色のテキストにはエスケープシーケンス `\033[32m` を使用し、赤色のテキストには `\033[31m` を使用しています。また、カラーリセットには `\033[0m` を使用して元のテキストカラーに戻しています。

なお、WindowsのコマンドプロンプトではANSIエスケープシーケンスがデフォルトで無効になっているため、上記のコードは一部のターミナルエミュレータや環境でのみ機能します。WindowsのコマンドプロンプトでANSIエスケープシーケンスを有効にするには、`colorama`といったライブラリを使用する必要があります。



## イクマの見解

ChatGPT の解説にもあるとおり colorama を使った方が便利なのでそれで実装してもらいます。



# 質問 ⑨

colorama ライブラリを使った実装にしてください。



# 回答 ⑨

了解しました。coloramaライブラリを使用してANSIエスケープシーケンスをWindowsのコマンドプロンプトでも有効にするようにコードを修正します。以下が修正後のコードです。

```py
import json
import os
from colorama import init, Fore

init()  # coloramaの初期化


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def get_json_file_list() -> list:
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files: list[str]):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files: list[str]) -> str:
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file: str) -> list[dict]:
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def get_user_answer() -> str:
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question: dict) -> bool:
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print(Fore.GREEN + "正解です！" + Fore.RESET)
        else:
            print(Fore.RED + "不正解です！" + Fore.RESET)
        print("\n解説:", question['explanation'])
        print("-" * os.get_terminal_size().columns)

    print("模擬試験が終了しました！")
    print("正解数:", correct_answers)
    print("正答率:", correct_answers / len(questions) * 100, "%")


if __name__ == '__main__':
    main()

```



修正後のコードでは、`colorama`ライブラリから`init`関数と`Fore`クラスをインポートし、初期化と色の設定を行っています。正解の文字列は`Fore.GREEN`で緑色に、不正解の文字列は`Fore.RED`で赤色に設定されます。また、文字列の色をリセットするために、正解・不正解の出力後に`Fore.RESET`を使用して元のテキストカラーに戻しています。

これにより、`colorama`ライブラリを使用してWindowsのコマンドプロンプトでも正解が緑色、不正解が赤色で表示されるようになります。



## 少し手を加えます

```py
print(Fore.GREEN + "正解です！" + Fore.RESET)
print(Fore.RED + "不正解です！" + Fore.RESET)
```

を

```py
print(f"{Fore.GREEN}正解です!{Fore.RESET}")
print(f"{Fore.RED}不正解です!{Fore.RESET}")
```

に直します。



さらに

```py
print(f"{Fore.BLUE}模擬試験が終了しました！{Fore.RESET}")
```

とし、何問中、何問正解したかも表示するようにします。

```py
print(f"{len(questions)}問中{correct_answers}問正解しました。")
```





また、正答率70%以上で合格、そうでないときに不合格と表示するよう以下の修正を行います。

```py
correct_answer_rate = correct_answers / len(questions) * 100
print("正答率:", correct_answer_rate, "%")

if correct_answer_rate >= 70:
    print(f"{Fore.GREEN}合格です！おめでとうございます！{Fore.RESET}")
else:
    print(f"{Fore.RED}不合格です。残念でした。{Fore.RESET}")
```



そして、colorma の初期化関数を コード冒頭から以下の場所に移動させます。

```py
if __name__ == '__main__':
    init()  # coloramaの初期化
    main()
```

外部から呼ばれるモジュールの場合、init()などが実行される実装になっていると思わぬ副作用が生じる可能性があるので `__name__ == '__main__'`の中に隔離します。 (この模擬試験アプリの場合外部から呼ばれることは想定していませんが)



次は演習問題が始まったときにターミナルに余計な情報(コマンド履歴)が表示されないように修正を加えます。



# 質問 ⑩

模擬試験が始まるタイミングでターミナルをクリアしてください。

```py
import json
import os

from colorama import init, Fore


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def get_json_file_list() -> list:
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files: list[str]):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files: list[str]) -> str:
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file: str) -> list[dict]:
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def get_user_answer() -> str:
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question: dict) -> bool:
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print(f"{Fore.GREEN}正解です!{Fore.RESET}")
        else:
            print(f"{Fore.RED}不正解です!{Fore.RESET}")
        print("\n解説:", question['explanation'])
        print("-" * os.get_terminal_size().columns)

    print(f"{Fore.BLUE}模擬試験が終了しました！{Fore.RESET}")
    print(f"{len(questions)}問中{correct_answers}問正解しました。")
    correct_answer_rate = correct_answers / len(questions) * 100
    print("正答率:", correct_answer_rate, "%")

    if correct_answer_rate >= 70:
        print(f"{Fore.GREEN}合格です！おめでとうございます！{Fore.RESET}")
    else:
        print(f"{Fore.RED}不合格です。残念でした。{Fore.RESET}")


if __name__ == '__main__':
    init()  # coloramaの初期化
    main()

```



# 回答 ⑩

上記のコードでは、coloramaライブラリを使用してターミナルをクリアするために`os.system('cls' if os.name == 'nt' else 'clear')`を使用しています。ターミナルをクリアするためには、このコードを模擬試験が始まる直前に追加する必要があります。以下が修正後のコードです。

```py
import json
import os
from colorama import init, Fore


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def get_json_file_list() -> list:
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files: list[str]):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files: list[str]) -> str:
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file: str) -> list[dict]:
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def get_user_answer() -> str:
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question: dict) -> bool:
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    correct_answers = 0

    # ターミナルをクリア
    os.system('cls' if os.name == 'nt' else 'clear')

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print(f"{Fore.GREEN}正解です!{Fore.RESET}")
        else:
            print(f"{Fore.RED}不正解です!{Fore.RESET}")
        print("\n解説:", question['explanation'])
        print("-" * os.get_terminal_size().columns)

    print(f"{Fore.BLUE}模擬試験が終了しました！{Fore.RESET}")
    print(f"{len(questions)}問中{correct_answers}問正解しました。")
    correct_answer_rate = correct_answers / len(questions) * 100
    print("正答率:", correct_answer_rate, "%")

    if correct_answer_rate >= 70:
        print(f"{Fore.GREEN}合格です！おめでとうございます！{Fore.RESET}")
    else:
        print(f"{Fore.RED}不合格です。残念でした。{Fore.RESET}")


if __name__ == '__main__':
    init()  # coloramaの初期化
    main()

```



## イクマの見解

ターミナルをクリアすることで余計な情報を非表示にできます。そのためのコードは1行で済みます。

```py
os.system('cls' if os.name == 'nt' else 'clear')
```

このコードを複数箇所使いたいのですが、このコードのままだと少し読みにくいです。そのため以下のように関数にし、名前を付けます。

```py
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
```



この関数を以下の場所に記述します。

```py
if __name__ == '__main__':
    init()  # coloramaの初期化
    clear_terminal()
    main()
```



もう一カ所にも記述します。

```python
def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)  # ここでクリア

    clear_terminal()
```



# 完成

これで完成です。プログラム全体のソースコードは以下のようになります。

```py
import json
import os

from colorama import init, Fore


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_question(question: dict):
    """
    問題を表示する

    :param question: 問題の辞書
    """
    print("問題ID:", question['id'])
    print("\n問題:", question['question'])
    print("\n選択肢:")
    for key, value in question['choices'][0].items():
        print(key + ':', value)


def get_json_file_list() -> list:
    """
    JSONファイルのリストを取得する

    :return: JSONファイルのリスト
    """
    json_files = [f for f in os.listdir('jsons') if f.endswith('.json')]
    if not json_files:
        print("'jsons'ディレクトリ内にJSONファイルが見つかりません。")
        return []
    json_files.reverse()  # リストを逆順にする
    return json_files


def display_file_options(json_files: list[str]):
    """
    ファイル番号の選択肢を表示する

    :param json_files: JSONファイルのリスト
    """
    print("番号を入力してJSONファイルを選択してください:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")


def get_user_choice(json_files: list[str]) -> str:
    """
    ユーザーの選択を受け付ける

    :param json_files: JSONファイルのリスト
    :return: 選択されたJSONファイルのパス
    """
    while True:
        try:
            choice = int(input("番号を入力してください: "))
            if choice < 1 or choice > len(json_files):
                raise ValueError
            break
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return json_files[choice - 1]


def load_questions(json_file: str) -> list[dict]:
    """
    問題を読み込む

    :param json_file: JSONファイルのパス
    :return: 問題のリスト
    """
    with open(os.path.join('jsons', json_file)) as f:
        questions = json.load(f)
    return questions


def get_user_answer() -> str:
    """
    ユーザーの回答を受け付ける

    :return: ユーザーの回答
    """
    while True:
        answer = input("\n回答を入力してください (A, B, C, D): ").upper()
        if answer not in ['A', 'B', 'C', 'D']:
            print("無効な回答です。A、B、C、Dのいずれかを入力してください。")
        else:
            return answer


def present_question(question: dict) -> bool:
    """
    問題を表示し、回答を受け付ける

    :param question: 問題の辞書
    :return: 回答が正解かどうか
    """
    display_question(question)
    answer = get_user_answer()
    return answer == question['answer']


def main():
    json_files = get_json_file_list()
    if not json_files:
        return

    display_file_options(json_files)

    selected_file = get_user_choice(json_files)

    questions = load_questions(selected_file)

    clear_terminal()

    correct_answers = 0

    # 問題を表示して回答を受け付ける
    for question in questions:
        if present_question(question):
            correct_answers += 1
            print(f"{Fore.GREEN}正解です!{Fore.RESET}")
        else:
            print(f"{Fore.RED}不正解です!{Fore.RESET}")
        print("\n解説:", question['explanation'])
        print("-" * os.get_terminal_size().columns)

    print(f"{Fore.BLUE}模擬試験が終了しました！{Fore.RESET}")
    print(f"{len(questions)}問中{correct_answers}問正解しました。")
    correct_answer_rate = correct_answers / len(questions) * 100
    print("正答率:", correct_answer_rate, "%")

    if correct_answer_rate >= 70:
        print(f"{Fore.GREEN}合格です！おめでとうございます！{Fore.RESET}")
    else:
        print(f"{Fore.RED}不合格です。残念でした。{Fore.RESET}")


if __name__ == '__main__':
    init()  # coloramaの初期化
    clear_terminal()
    main()

```

