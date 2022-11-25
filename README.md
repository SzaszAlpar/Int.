# Int.

Am rezolvat problema în două moduri, ambele în Python.

În prima rezolvare (p1.py) am folosit pachetul Pandas. Avantajul a fost faptul că am reușit să citesc toată data dintr-o singură comandă, iar manipularea acesteia mi-a fost ușurată datorită unor methode cum ar fi DataFrame.GroupBy. Fiindcă am folosit pandas, am putut să acceses unele informații direct cu titlul coloanei respective, nu a trebuit să acord o atenție faptului că în unele input-uri poate coloanele să nu fie puse mereu în aceeași ordine.

În a doua rezolvare (p2.py) nu am importat niciun alt pachet. Am citit fisierul CSV cu methoda ReadLine. A trebuit să identific coloanele care îmi erau importante apoi să grupez datele cu ajutorul unui dictionary.

Consider că ambele rezolvări sunt bune, deși eu prefer utilizarea pachetului Pandas pentru a ne ușura unele taskuri și pentru eleganța codului.


HOW TO RUN:
Programul este un simplu code Python, se poate folosi și din cmd astfel:
Python p1.py
Python p2.py

Programul așteaptă ca și input numele unui singur fișier (tot cu domeniul ".csv" ). Fișier care se află în același folder ca și code-ul. Rezultatul apare în consolă dar și în output.txt. 
După rezultat se poate introduce un alt nume de input. Programul se încheie cu inputul "q".

EXEMPLU:
$ Python p2_copy.py

"Service started!
Press 'q' to exit.

Please enter file name: input2.csv"
