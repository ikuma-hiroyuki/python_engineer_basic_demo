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
