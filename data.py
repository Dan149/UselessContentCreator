import random
import secrets
import string
from english_words import english_words_set as words
words = list(words)
names = ["document", "presentation", "repo", "album", "work", "printable", "homework", "game", "ideas", "idea", "business", "personnal", "private", "public", "useful", "content", "secret", "internet", "demo", "diaporama", "test", "no-use", "file", "text", "picture", "video", "music", "youtube", "amazon", "google", "microsoft", "gmail", "firefox", "yahoo", "outlook", "browser", "password", "list", "numbers", "bank", "info", "information", "account", "user", "turtles", "turtle", "admin", "supervisor", "secretary", "corporation", "brainstorm", "earth", "brain", "core", "main", "security", "cache", "data", "database", "history", "user-info", "github", "gitlab", "random", "default", "translation", "french", "spanish", "italian", "russian", "english", "indian", "map", "geolocation", "ip-address", "userconfig", "hash", "hashes", "passwords", "secrets", "friends", "girlfriend", "wedding", "love", "script", "urgent", "warning", "todo", "cash", "bank-account", "bank-info", "credits", "credentials", "oscars", "pmkid", "wifi-config", "handshake", "handshakes", "wpa", "wep", "aircrack", "nmap", "metasploit", "msf", "recon", "military", "nikto", "trash", "garbage", "apple", "mac", "iphone", "guns", "money", "2FA", "phone-password", "laptop-password", "server", "laptop", "client", "cloud", "icloud", "twitch", "troll", "fake", "project-v1", "project", "project-v2", "unknown", "artist", "copyright", "copyrights", "visa", "mastercard", "bitcoin", "litecoin", "ethereum", "monero", "doge", "coinbase", "binance", "eminem", "dr.dre", "snoop", "snoop-dogg", "example", "e-sport", "esports", "live", "puns", "log", "logs", "email", "mail", "address", "press", "utils", "plain-text", "school", "class", "motherland", "save", "backup", "tips", "paypal", "free", "sale", "premium-account", "premium", "lobby", "hobby", "job", "merch", "new", "license", "free", "style", "brand", "company", "incorporation",, "init", "root", "amazon", "delivery", "coins"]
site_titles = ["My Site", "My Shop", "Web Site", "Google", "Outlook", "Yahoo!", "Yandex", "Search", "website", "Unknown", "Random", "Example", "Sample", "Github", "Gitlab", "Minecraft", "Rainbow Six", "Game", "JavaScript", "Wordpress", "Word Press", "Internet", "Browser", "Index", "Blank", "about:blank", "Server", "Trash", "Save", "Backup", "Spam", "Mailbox", "Wiki", "Wikipedia", "Youtube", "Youtube Kids", "Premium account", "All safe", "Pokemon", "Linux", "Human ressources", "Turtles", "Init", "Geography", "Congratulations", "Warning", "Amazon", "Coins"]
fonts = ["Times", "Courier", "Helvetica", "Arial"]

def flush_doc_content():
	doc_content = ''.join(secrets.choice(words) + " " for i in range(random.randint(5000, 100000)))
	return doc_content

def flush_alternative():
    doc_content = ''.join(secrets.choice(string.printable) for i in range(random.randint(10000, 5000000)))
    return doc_content

def html_template(title, content, script, version):
    print(f"html style format version: {version}")
    colors = ["blue", "skyblue", "green", "darkgreen", "darkred", "darkblue", "orange", "grey", "darkorange", "darkgrey", "indianred", "darkolivegreen", "greenyellow", "limegreen", "seagreen", "forestgreen", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
    fonts = ["Times-Roman", "Helvetica", "Arial", "dubai", "Algerian", "Broadway", "Carlito", "Cantarell", "ahori"]
    color = secrets.choice(colors)
    font = secrets.choice(fonts)
    if script != None and version == 1:
        html_doc = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>{}</title>
</head>
<body style='color:{}; font-family:{};'>
<p>
{}
</p>
<script>{}</script>
</body>
</html>""".format(title, color, font, content, script)

    elif script == None and version == 1:
        html_doc = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>{}</title>
</head>
<body style='color:{}; font-family:{};'>
{}
</body>
</html>""".format(title, color, font, content)

# html page style format v2:
    elif script != None and version == 2: # with JS
        html_doc2 = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{}</title>
</head>
<body>
<h1 style='color:{}; font-family:{};'><h1><br>
    <p>
        <p>{}</p>
    <br>
        <p>{}</p>
    </p>
</body>
</html> """.format(title, color, font, content1, content2)
    elif script == None and version == 2: # without JS
        html_doc = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{}</title>
</head>
<body>
<h1 style='color:{}; font-family:{};'><h1><br>
    <p>
        <p>{}</p>
    <br>
        <p>{}</p>
    </p>
</body>
</html> """.format(title, color, font, content, content)
    else:
        print("[ERROR]: issue with the html_template() function")
    return html_doc