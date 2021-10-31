# LLS-Softwareprojekt

Dieses Repository beinhaltet alle nötigen Quelldateien zum Start eines ARP-Covert-Channels.

Zum Start des Programms wird folgender Befehl benötigt:

``` python .\main.py ```

Um das Programm zu stoppen, ist lediglich ein User-Interrupt mittels ``` Ctrl+C ``` im Kommandozeilenfenster des Programmes notwendig.


## Benötigte Python-Module
* [pycryptodome](https://pypi.org/project/pycryptodome/)
* [scapy v. 2.44](https://pypi.org/project/scapy/)
* [Flask](https://pypi.org/project/Flask/)
* [Flask-Socketio](https://pypi.org/project/Flask-SocketIO/)
* [Flask-Cors](https://pypi.org/project/Flask-Cors/)
* [eventlet](https://pypi.org/project/eventlet/)
* [requests](https://pypi.org/project/requests/)
* [websocket-client](https://pypi.org/project/websocket-client/)


## Dateien und Ordner

#### FrontendSWP
Dieser Ordner beinhaltet die unkompilierten Angular und Bootstrap Quelldateien zur Darstellung des webbasierten Frontends.

#### Unit Tests
Dieser Ordner beinhaltet die Unit-Tests zum Testen von Kodierung und Verschlüsselung des Programms.

#### static
Dieser Ordner enthält die kompilierten Javascript-Dateien, um die Webseite mithilfe des Flask-Webservers zu rendern.

#### templates
Dieser Ordner enthält die Template-HTML-Datei, welche als Renderdatei vom Webserver verwendet wird.

#### MessagePrepTimes
Diese Datei beinhaltet die gemessenen Zeiten zur Nachrichtenvorbereitung vor dem Absenden der Nachrichten. Es wird hier sowohl die geschickte Nachricht, als auch die benötigte Zeit festgehalten.

#### arp_receiver.py
Diese Datei beinhaltet die Implementierung der Empfängerseite des Covert-Channels und ist für das Filtern und Extrahieren der Nachricht aus einem empfangenen ARP-Packet zuständig.

#### arp_sender.py
Diese Datei beinhaltet die Implementierung der Senderseite des Cover-Channels und ist für das Senden von kodierten und verschlüsselten Nachrichten in ARP-Packeten zuständig.

#### encode_decode.py
Diese Datei enthält die Umsetzung der Kodierung und Dekodierung von Klartext-Nachrichten, um diese einem MAC-Adressen-Format anzupassen.

#### encrypt_decrypt.py
Diese Datei enthält die Umsetzung der Verschlüsselung und Entschlüsselung von Klartext-Nachrichten mithilfe des symmetrischen AES-Verschlüsselungsverfahrens im ECB-Modus.

#### file_functions.py
Diese Datei beinhaltet Funktionen zum Speichern von Daten in Dateien und dem Lesen von Daten aus Dateien. Zum jetzigen Stand der Implementierung wird diese Datei nicht verwendet.

#### main.py
Start des Programms

#### webserver_flask_websocket.py
Diese Datei beinhaltet die Umsetzung des Flask-Webservers inklusive des Websockets.
