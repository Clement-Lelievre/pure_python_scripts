import dns.resolver as d
import requests, time
from colorama import init, Fore

'''this script tries to connect to inputted websites using their IP adress and returns whether it is feasible or not'''

print('Warning: just because HTTP status code is 200 does not mean you get the intended webpage; it only means the GET request worked well.\n')
#setting up colorama (text colouring in the shell)
init()
GREEN = Fore.GREEN
RED   = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

starttime = time.time()
# websites to test
websites_list  = ['lemonde.fr','google.com','liberation.fr','chess.com','chess24.com','youtube.com','amazon.com','lewagon.com','apple.com','microsoft.com']
ip_dict = {url:'' for url in websites_list}

for url in websites_list:
    try:
        ips = [str(item) for item in d.resolve(url, 'A')]
        ip = ips[0]
        ip_dict[url] = ips
        s = requests.get('http://' + ip).status_code
        if s == 200:
            print(f'{GREEN}Connection to {url} via (first) IP in searchbar works! {RESET}\n')
        else:
            print(f'{RED}Connection to {url} via (first) IP in searchbar yields HTTP error number {s} {RESET}\n')
    except Exception: 
        # if only 'except:' had been written here, Ctrl+C would not have been possible to end prematurely the script,
        # as the Keyboardinterruptexception would have been caught by this 'except:'
        print(f'{YELLOW}Connection to {url} via (first) IP in searchbar failed! {RESET}\n')
    except KeyboardInterrupt:
        print('iao!') # if user presses Ctrl + C, sheel print ^C and as a little joke I use this C to print Ciao
        quit()
        
        
endtime = time.time()
t = endtime - starttime
print(f'Done in {round(t,1)} seconds.\n')
print(ip_dict)
