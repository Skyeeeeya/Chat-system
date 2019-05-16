
from chat_client_class import *
from GUI_LOGIN import *

def main():
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()

    client = Client(args)
    window.mainloop()
    client.run_chat()

main()
