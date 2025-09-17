# load_env.py


def main():
    from dotenv import load_dotenv
    import os

    # 默认会去找当前目录下的 .env 文件并全部注入到 os.environ
    load_dotenv()

    # 演示读取
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    print('OPENAI_API_KEY =', OPENAI_API_KEY)
    MODEL_NAME = os.getenv('MODEL_NAME')
    print('MODEL_NAME =', MODEL_NAME)
    OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
    print('OPENAI_API_BASE =', OPENAI_API_BASE)


if __name__ == "__main__":
    main()