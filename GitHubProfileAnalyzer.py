import requests
from colorama import Fore, Style, init

init(autoreset=True)

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"{Fore.CYAN}👤 Username: {Style.BRIGHT}{user_data['login']}")
        print(f"{Fore.YELLOW}📂 Public Repos: {Style.BRIGHT}{user_data['public_repos']}")
        print(f"{Fore.GREEN}⭐ Followers: {Style.BRIGHT}{user_data['followers']}")
        print(f"{Fore.MAGENTA}📡 Following: {Style.BRIGHT}{user_data['following']}")
        print(f"{Fore.BLUE}🗓️ Account Created: {Style.BRIGHT}{user_data['created_at']}")
    else:
        print(f"{Fore.RED}❌ Error fetching profile. Check the username.")

def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f"\n{Fore.CYAN}Repositories for {Style.BRIGHT}{username}:{Style.RESET_ALL}")
        for repo in repos[:10]: 
            print(f"{Fore.YELLOW}📘 {Style.BRIGHT}{repo['name']} - {Fore.GREEN}⭐ {repo['stargazers_count']} stars")
    else:
        print(f"{Fore.RED}❌ Error fetching repositories.")

username = input(f"{Fore.CYAN}Enter GitHub username: {Style.RESET_ALL}")
fetch_github_profile(username)
fetch_repositories(username)
