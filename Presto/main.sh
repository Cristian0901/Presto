#!/bin/bash

ESC=$(printf '\033')
RESET="${ESC}[0m"
GREEN="${ESC}[32m"
YELLOW="${ESC}[33m"
BLUE="${ESC}[34m"
MAGENTA="${ESC}[35m"
CYAN="${ESC}[36m"
RED="${ESC}[31m" #WHITE="${ESC}[37m" DEFAULT="${ESC}[39m"

ok() {
    printf "${GREEN}%s${RESET}\n" "$1"
    }
name() { 
    printf "${BLUE}%s${RESET}\n" "$1"
}
error() { 
    printf "${RED}%s${RESET}\n" "$1"
}
alert() { 
    printf "${YELLOW}%s${RESET}\n" "$1"
}
magentaprint() { 
    printf "${MAGENTA}%s${RESET}\n" "$1"
}
cyanprint() { 
    printf "${CYAN}%s${RESET}\n" "$1"
}
    
create_project(){
    PS3="Select a language: "
    commands=("Python" "C/C++" "Rust" "Shell")
    select opt in "${commands[@]}"; do
        case $opt in
            "Python")
                echo "$YELLOW Language: $GREEN  Python $RESET"
                cp -R "./template/python/" "$2"
                shift 1
                break;;
            "C/C++")
                echo "$YELLOW Language: $GREEN C/C++ $RESET"
                shift 1
                break;;
            "Rust")
                echo "$YELLOW Language: $GREEN  Rust $RESET"
                shift 1
                break;;
            "Shell")
                echo "$YELLOW Language: $GREEN  Shell $RESET"
                shift 1
                break;;
            *)
                echo "$RED [ERROR]: $REPLY is a invalid option... $RESET";;
        esac
    done
    
}

case $1 in
    "create")
        if [ "$2" == "" ]; then
            echo "$RED [ERROR]: Empty project name... $RESET"
        elif [ "$2" == " " ]; then
            echo "$RED [ERROR]: Empty project name... $RESET"
        else
            echo "$YELLOW Project: $GREEN $2 $RESET"
            create_project "$3"
        fi
        ;;
    "help")
        #echo "...COMMAND...|...PARAMETERS...|.....DESCRIPTION....."
        #echo "   create    |  name: string  | Start a new project "
        #echo "   help      |       ...      |  Show this message  "
        {
            echo -e "COMMAND,PARAMETERS,DESCRIPTION\n" \
                    "create,name: string,Start a new project" \
                    "help,...,Show this message"
        } | column -t -s","
        ;;
    *)
        echo "$RED [ERROR]: Invalid command... $RESET"
        echo "$RED [ERROR]: Use 'help' for more information... $RESET"
        ;;
esac

