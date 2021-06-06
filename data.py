import random
import secrets
import string

names = ["document", "presentation", "repo", "album", "work", "printable", "homework", "game", "ideas", "idea", "business", "personnal", "private", "public", "useful", "content", "secret", "internet", "demo", "diaporama", "test", "no-use", "file", "text", "picture", "video", "music", "youtube", "amazon", "google", "microsoft", "gmail", "firefox", "yahoo", "outlook", "browser", "password", "list", "numbers", "bank", "info", "information", "account", "user", "admin", "supervisor", "secretary", "corporation", "brainstorm", "earth", "brain", "core", "main", "security", "cache", "data", "database", "history", "user-info", "github", "gitlab", "random", "default", "translation", "french", "spanish", "italian", "russian", "english", "indian", "map", "geolocation", "ip-address", "userconfig", "hash", "hashes", "passwords", "secrets", "friends", "girlfriend", "wedding", "love", "script", "urgent", "warning", "todo", "cash", "bank-account", "bank-info", "credits", "credentials", "oscars", "pmkid", "wifi-config", "handshake", "handshakes", "wpa", "wep", "aircrack", "nmap", "metasploit", "msf", "recon", "military", "nikto", "trash", "garbage", "apple", "mac", "iphone", "guns", "money", "2FA", "phone-password", "laptop-password", "server", "laptop", "client", "cloud", "icloud", "twitch", "troll", "fake", "project-v1", "project", "project-v2", "unknown", "artist", "copyright", "copyrights", "visa", "mastercard", "bitcoin", "litecoin", "ethereum", "monero", "doge", "coinbase", "binance", "eminem", "dr.dre", "snoop", "snoop-dogg"]
site_titles = ["My Site", "My Shop", "Web Site", "Google", "Outlook", "Yahoo!", "Yandex", "Search", "website", "Unknown", "Random", "UCC", "Example", "Sample", "Github", "Gitlab", "Minecraft", "Rainbow Six", "Game", "JavaScript"]

def flush_doc_content():
	doc_content = ''.join(secrets.choice(string.printable) for i in range(random.randint(1000, 1000000)))
	return doc_content

def html_template(title, content, script):
	if script != None:
		html_doc = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>{}</title>
</head>
<body>
{}
<script>{}</script>
</body>
</html>""".format(title, content, script)

	else:
		html_doc = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>{}</title>
</head>
<body>
{}
</body>
</html>""".format(title, content)
	return html_doc