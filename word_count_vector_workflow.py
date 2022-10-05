= RESTART: C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py
Articles collected!
>>> from collections import Counter
>>> total_counts = Counter()
>>> total_counts["the"]
0
>>> len(all_article_data)
998
>>> for article_title in all_article_data:
	article_counts = word_counts(article_title)
	for word in article_counts:
		total_counts[word] += article_counts[word]

		
Traceback (most recent call last):
  File "<pyshell#203>", line 2, in <module>
    article_counts = word_counts(article_title)
  File "C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py", line 156, in word_counts
    return {word: text.count(word) for word in words}
  File "C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py", line 156, in <dictcomp>
    return {word: text.count(word) for word in words}
KeyboardInterrupt
>>> for article_title in all_article_data:
	print(article_title)
	article_counts = word_counts(article_title)
	for word in article_counts:
		total_counts[word] += article_counts[word]
		
KeyboardInterrupt
>>> total_counts = Counter()
>>> total_counts["the"]
0
>>> for article_title in all_article_data:
	print(article_title)
	article_counts = word_counts(article_title)
	for word in article_counts:
		total_counts[word] += article_counts[word]

		
0
Abiogenesis
Abortion
Abraham Lincoln
Abraham
Abstract algebra
Abstract art
Achaemenid Empire
Acid-base reaction
Adam Smith
Addiction
Adi Shankara
Adolescence
Traceback (most recent call last):
  File "<pyshell#211>", line 3, in <module>
    article_counts = word_counts(article_title)
  File "C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py", line 156, in word_counts
    return {word: text.count(word) for word in words}
  File "C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py", line 156, in <dictcomp>
    return {word: text.count(word) for word in words}
KeyboardInterrupt
>>> from pandas.io import clipboard
>>> titles = clipboard.paste().split('\r\n')
>>> themes = clipboard.paste().split('\r\n')
>>> themes[-1]
''
>>> len(titles)
1000
>>> titles = titles[1:-1]
>>> themes = themes[1:-1]
>>> x = set(themes)
>>> x
{'Geography', 'Science', 'Technology', 'History', 'Health, medicine and disease', 'Everyday life', 'Arts', 'Philosophy and religion', 'Society and social sciences', 'Mathematics', 'People'}
>>> len(x)
11
>>> d = {theme:[] for theme in x}
>>> page_lists = d
>>> for title, theme in zip(titles, themes):
	page_lists[theme].append(title)

	
>>> page_lists["Mathematics"]
['Mathematics', 'Algorithm', 'Mathematical proof', 'Set (mathematics)', 'Function (mathematics)', 'Combinatorics', 'Number', 'Real number', 'E (mathematical constant)', 'Pi', 'Fraction', 'Integer', '0', 'Natural number', 'Prime number', 'Complex number', 'Number theory', 'Algebra', 'Equation', 'Variable (mathematics)', 'Linear algebra', 'Abstract algebra', 'Mathematical analysis', 'Calculus', 'Infinity', 'Limit (mathematics)', 'Series (mathematics)', 'Arithmetic', 'Exponentiation', 'Logarithm', 'Nth root', 'Geometry', 'Angle', 'Trigonometry', 'Area', 'Conic section', 'Circle', 'Line (geometry)', 'Polygon', 'Triangle', 'Three-dimensional space', 'Volume', 'Topology', 'Probability', 'Statistics']
>>> clipboard.copy(page_lists)
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    clipboard.copy(page_lists)
  File "C:\Users\Alastair\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\io\clipboard\__init__.py", line 444, in copy_windows
    text = _stringifyText(text)  # Converts non-str values to str.
  File "C:\Users\Alastair\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\io\clipboard\__init__.py", line 104, in _stringifyText
    raise PyperclipException(
pandas.io.clipboard.PyperclipException: only str, int, float, and bool values can be copied to the clipboard, not dict
>>> clipboard.copy(str(page_lists))
>>> thematic_word_counts = {theme:Counter() for theme in page_lists}
>>> current_theme = "Mathematics"
>>> for article_name in page_lists[current_theme]:
	print(article_name)
	article_word_counts = word_counts(article_name)
	for word in article_word_counts:
		thematic_word_counts[current_theme][word] += article_word_counts[word]

		
Mathematics
Algorithm
Mathematical proof
Set (mathematics)
Function (mathematics)
Combinatorics
Number
Real number
E (mathematical constant)
Pi
Fraction
Integer
0
Natural number
Prime number
Complex number
Number theory
Algebra
Equation
Variable (mathematics)
Linear algebra
Abstract algebra
Mathematical analysis
Calculus
Infinity
Limit (mathematics)
Series (mathematics)
Arithmetic
Exponentiation
Logarithm
Nth root
Geometry
Angle
Trigonometry
Area
Conic section
Circle
Line (geometry)
Polygon
Triangle
Three-dimensional space
Volume
Topology
Probability
Statistics
>>> thematic_word_counts["mathematics"]["the"]
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    thematic_word_counts["mathematics"]["the"]
KeyError: 'mathematics'
>>> thematic_word_counts["Mathematics"]["the"]
15402
>>> thematic_word_counts["Mathematics"]["limit"]
191
>>> thematic_word_counts["Mathematics"]["pi"]
87
>>> thematic_word_counts["Mathematics"]["topological"]
89
>>> thematic_word_counts["Mathematics"]["Pi"]
0
>>> thematic_word_counts["Mathematics"]["tau"]
6
>>> thematic_word_counts = {theme:Counter() for theme in page_lists}
>>> for current_theme in thematic_word_counts:
	i = 0
	for article_name in page_lists[current_theme]:
		i += 1
		print(article_name, f"{i}/{len(page_lists[current_theme]}")
		article_word_counts = word_counts(article_name)
		for word in article_word_counts:
			thematic_word_counts[current_theme][word] += article_word_counts[word]
			
SyntaxError: f-string: closing parenthesis '}' does not match opening parenthesis '('
>>> for current_theme in thematic_word_counts:
	i = 0
	for article_name in page_lists[current_theme]:
		i += 1
		print(article_name, f"{i}/{len(page_lists[current_theme])}")
		article_word_counts = word_counts(article_name)
		for word in article_word_counts:
			thematic_word_counts[current_theme][word] += article_word_counts[word]

			
Geography 1/106
Continent 2/106
Africa 3/106
Antarctica 4/106
Asia 5/106
Europe 6/106
North America 7/106
South America 8/106
Arctic 9/106
Caribbean 10/106
Middle East 11/106
Oceania 12/106
Land 13/106
Desert 14/106
Sahara 15/106
Forest 16/106
Amazon rainforest 17/106
Grassland 18/106
Island 19/106
Mountain 20/106
Alps 21/106
Andes 22/106
Himalayas 23/106
Rocky Mountains 24/106
Sea 25/106
Arctic Ocean 26/106
Atlantic Ocean 27/106
Mediterranean Sea 28/106
Indian Ocean 29/106
Pacific Ocean 30/106
Great Barrier Reef 31/106
Southern Ocean 32/106
Lake 33/106
Caspian Sea 34/106
Great Lakes 35/106
Lake Victoria 36/106
River 37/106
Amazon River 38/106
Ganges 39/106
Mississippi River 40/106
Nile 41/106
Yangtze 42/106
Glacier 43/106
Country 44/106
Algeria 45/106
Democratic Republic of the Congo 46/106
Egypt 47/106
Ethiopia 48/106
Kenya 49/106
Nigeria 50/106
South Africa 51/106
Tanzania 52/106
Bangladesh 53/106
China 54/106
India 55/106
Indonesia 56/106
Iran 57/106
Israel 58/106
Japan 59/106
Malaysia 60/106
Myanmar 61/106
Pakistan 62/106
Philippines 63/106
Saudi Arabia 64/106
South Korea 65/106
Taiwan 66/106
Thailand 67/106
United Arab Emirates 68/106
Vietnam 69/106
Russia 70/106
Turkey 71/106
France 72/106
Germany 73/106
Italy 74/106
Netherlands 75/106
Poland 76/106
Spain 77/106
Ukraine 78/106
United Kingdom 79/106
Canada 80/106
Mexico 81/106
United States 82/106
Australia 83/106
Argentina 84/106
Brazil 85/106
Colombia 86/106
City 87/106
Cairo 88/106
Lagos 89/106
Beijing 90/106
Hong Kong 91/106
Tokyo 92/106
Jakarta 93/106
Singapore 94/106
Delhi 95/106
Mumbai 96/106
Istanbul 97/106
Jerusalem 98/106
Mecca 99/106
London 100/106
Moscow 101/106
Paris 102/106
Rome 103/106
Mexico City 104/106
New York City 105/106
SÃ£o Paulo 106/106
Traceback (most recent call last):
  File "<pyshell#249>", line 6, in <module>
    article_word_counts = word_counts(article_name)
  File "C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py", line 151, in word_counts
    article_data = get_article_data_from_file(article_name)
  File "C:\Users\Alastair\Documents\A - MSc\Data Mining & Machine Learning\wikipedia_page_data_fetcher.py", line 109, in get_article_data_from_file
    with open(f"articles\\{article_name}.txt", encoding="utf-8") as article_file:
FileNotFoundError: [Errno 2] No such file or directory: 'articles\\SÃ£o Paulo.txt'
>>> thematic_word_counts = {theme:Counter() for theme in page_lists}
>>> len(article_counts)
2209
>>> type(article_counts)
<class 'dict'>
>>> list(article_counts.keys())[0]
''
>>> list(article_counts.keys())[1]
'reasoning'
>>> list(article_counts.keys())[2]
"vedanta.shankara's"
>>> list(article_counts.keys())[3]
'mandala.the'
>>> list(article_counts.keys())[4]
'mayeda'
>>> list(article_counts.keys())[-1]
'telugu-language'
>>> L = []
>>> for x in page_lists.keys()L
SyntaxError: invalid syntax
>>> for x in page_lists.keys():
	L += x

	
>>> len(L)
145
>>> L[0]
'G'
>>> L[1]
'e'
>>> ''.join(L)
'GeographyScienceTechnologyHistoryHealth, medicine and diseaseEveryday lifeArtsPhilosophy and religionSociety and social sciencesMathematicsPeople'
>>> L = []
>>> for x in page_lists.values():
	L += x

	
>>> len(L)
998
>>> L[0]
'Geography'
>>> L[1]
'Continent'
>>> L[-1]
'Henry Ford'
>>> article_names = L
>>> import string
>>> L = [name for name in article_names if set(name+string.ascii_letters+' ') != set(string.ascii_letters+' ')]
>>> len(L)
29
>>> L
['SÃ£o Paulo', 'Mercury (planet)', "Newton's laws of motion", 'Cell (biology)', 'Taxonomy (biology)', 'Acidâ€“base reaction', 'Rock (geology)', 'Pre-Columbian era', 'Post-classical history', 'HIV_AIDS', 'Play (activity)', 'Realism (arts)', 'Power (social and political)', 'State (polity)', 'Indo-European languages', 'Set (mathematics)', 'Function (mathematics)', 'E (mathematical constant)', '0', 'Variable (mathematics)', 'Limit (mathematics)', 'Series (mathematics)', 'Line (geometry)', 'Three-dimensional space', 'SimÃ³n BolÃ\xadvar', 'NiccolÃ² Machiavelli', 'RenÃ© Descartes', 'Muhammad ibn Musa al-Khwarizmi', 'Kurt GÃ¶del']
>>> L = [name for name in article_names if set(name+string.ascii_letters+" ()'") != set(string.ascii_letters+" ()'")]
>>> L
['SÃ£o Paulo', 'Acidâ€“base reaction', 'Pre-Columbian era', 'Post-classical history', 'HIV_AIDS', 'Indo-European languages', '0', 'Three-dimensional space', 'SimÃ³n BolÃ\xadvar', 'NiccolÃ² Machiavelli', 'RenÃ© Descartes', 'Muhammad ibn Musa al-Khwarizmi', 'Kurt GÃ¶del']
>>> L = [name for name in article_names if set(name+string.ascii_letters+" ()'") != set(string.ascii_letters+" ()'"-)]
SyntaxError: invalid syntax
>>> L = [name for name in article_names if set(name+string.ascii_letters+" ()'") != set(string.ascii_letters+" ()'-")]
>>> L

>>> L = [name for name in article_names if set(name+string.ascii_letters+" ()'-") != set(string.ascii_letters+" ()'-")]
>>> L
['SÃ£o Paulo', 'Acidâ€“base reaction', 'HIV_AIDS', '0', 'SimÃ³n BolÃ\xadvar', 'NiccolÃ² Machiavelli', 'RenÃ© Descartes', 'Kurt GÃ¶del']
>>> page_lists.replace('SÃ£o Paulo', 'São Paulo')
Traceback (most recent call last):
  File "<pyshell#290>", line 1, in <module>
    page_lists.replace('SÃ£o Paulo', 'São Paulo')
AttributeError: 'dict' object has no attribute 'replace'
>>> page_lists["Geography"].replace('SÃ£o Paulo', 'São Paulo')
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    page_lists["Geography"].replace('SÃ£o Paulo', 'São Paulo')
AttributeError: 'list' object has no attribute 'replace'
>>> page_lists = {theme:[] for theme in x}
>>> titles = clipboard.paste().split('\r\n')
>>> themes = clipboard.paste().split('\r\n')
>>> len(titles)
1000
>>> titles = titles[1:-1]; themes = themes[1:-1]
>>> for title, theme in zip(titles, themes):
	page_lists[theme].append(title)

	
Traceback (most recent call last):
  File "<pyshell#298>", line 2, in <module>
    page_lists[theme].append(title)
KeyError: 'People'
>>> page_lists
{'Hammurabi': [], 'Hatshepsut': [], 'Ramesses II': [], 'Cyrus the Great': [], 'Alexander the Great': [], 'Ashoka': [], 'Qin Shi Huang': [], 'Julius Caesar': [], 'Augustus': [], 'Charlemagne': [], 'Genghis Khan': [], 'Mansa Musa': [], 'Joan of Arc': [], 'Suleiman the Magnificent': [], 'Akbar': [], 'Elizabeth I': [], 'Catherine the Great': [], 'George Washington': [], 'Napoleon': [], 'SimÃ³n BolÃ\xadvar': [], 'Abraham Lincoln': [], 'Mahatma Gandhi': [], 'Joseph Stalin': [], 'Adolf Hitler': [], 'Mao Zedong': [], 'Nelson Mandela': [], 'Abraham': [], 'Moses': [], 'Gautama Buddha': [], 'Jesus': [], 'Paul the Apostle': [], 'Muhammad': [], 'Adi Shankara': [], 'Martin Luther': [], 'Marco Polo': [], 'Zheng He': [], 'Christopher Columbus': [], 'Vasco da Gama': [], 'Ferdinand Magellan': [], 'James Cook': [], 'Roald Amundsen': [], 'Confucius': [], 'Laozi': [], 'Herodotus': [], 'Socrates': [], 'Plato': [], 'Aristotle': [], 'Cicero': [], 'Thomas Aquinas': [], 'Ibn Khaldun': [], 'NiccolÃ² Machiavelli': [], 'RenÃ© Descartes': [], 'John Locke': [], 'Adam Smith': [], 'Immanuel Kant': [], 'Mary Wollstonecraft': [], 'Karl Marx': [], 'Friedrich Nietzsche': [], 'Sigmund Freud': [], 'Homer': [], 'Virgil': [], 'Li Bai': [], 'Murasaki Shikibu': [], 'Rumi': [], 'Dante Alighieri': [], 'Miguel de Cervantes': [], 'William Shakespeare': [], 'Voltaire': [], 'Leo Tolstoy': [], 'Rabindranath Tagore': [], 'Leonardo da Vinci': [], 'Michelangelo': [], 'Rembrandt': [], 'Hokusai': [], 'Pablo Picasso': [], 'Frida Kahlo': [], 'Johann Sebastian Bach': [], 'Wolfgang Amadeus Mozart': [], 'Ludwig van Beethoven': [], 'Louis Armstrong': [], 'The Beatles': [], 'Michael Jackson': [], 'Hippocrates': [], 'Avicenna': [], 'Shen Kuo': [], 'Johannes Gutenberg': [], 'Nicolaus Copernicus': [], 'Galileo Galilei': [], 'Isaac Newton': [], 'Carl Linnaeus': [], 'Antoine Lavoisier': [], 'Michael Faraday': [], 'Charles Darwin': [], 'Florence Nightingale': [], 'Louis Pasteur': [], 'James Clerk Maxwell': [], 'Dmitri Mendeleev': [], 'Thomas Edison': [], 'Nikola Tesla': [], 'Marie Curie': [], 'Albert Einstein': [], 'Archimedes': [], 'Euclid': [], 'Muhammad ibn Musa al-Khwarizmi': [], 'Leonhard Euler': [], 'Carl Friedrich Gauss': [], 'Emmy Noether': [], 'Kurt GÃ¶del': [], 'Alan Turing': [], 'Charlie Chaplin': [], 'Walt Disney': [], 'Henry Ford': []}
>>> themes = clipboard.paste().split('\r\n')
>>> themes = themes[1:-1]
>>> page_lists = {theme:[] for theme in x}
>>> page_lists
{'Hammurabi': [], 'Hatshepsut': [], 'Ramesses II': [], 'Cyrus the Great': [], 'Alexander the Great': [], 'Ashoka': [], 'Qin Shi Huang': [], 'Julius Caesar': [], 'Augustus': [], 'Charlemagne': [], 'Genghis Khan': [], 'Mansa Musa': [], 'Joan of Arc': [], 'Suleiman the Magnificent': [], 'Akbar': [], 'Elizabeth I': [], 'Catherine the Great': [], 'George Washington': [], 'Napoleon': [], 'SimÃ³n BolÃ\xadvar': [], 'Abraham Lincoln': [], 'Mahatma Gandhi': [], 'Joseph Stalin': [], 'Adolf Hitler': [], 'Mao Zedong': [], 'Nelson Mandela': [], 'Abraham': [], 'Moses': [], 'Gautama Buddha': [], 'Jesus': [], 'Paul the Apostle': [], 'Muhammad': [], 'Adi Shankara': [], 'Martin Luther': [], 'Marco Polo': [], 'Zheng He': [], 'Christopher Columbus': [], 'Vasco da Gama': [], 'Ferdinand Magellan': [], 'James Cook': [], 'Roald Amundsen': [], 'Confucius': [], 'Laozi': [], 'Herodotus': [], 'Socrates': [], 'Plato': [], 'Aristotle': [], 'Cicero': [], 'Thomas Aquinas': [], 'Ibn Khaldun': [], 'NiccolÃ² Machiavelli': [], 'RenÃ© Descartes': [], 'John Locke': [], 'Adam Smith': [], 'Immanuel Kant': [], 'Mary Wollstonecraft': [], 'Karl Marx': [], 'Friedrich Nietzsche': [], 'Sigmund Freud': [], 'Homer': [], 'Virgil': [], 'Li Bai': [], 'Murasaki Shikibu': [], 'Rumi': [], 'Dante Alighieri': [], 'Miguel de Cervantes': [], 'William Shakespeare': [], 'Voltaire': [], 'Leo Tolstoy': [], 'Rabindranath Tagore': [], 'Leonardo da Vinci': [], 'Michelangelo': [], 'Rembrandt': [], 'Hokusai': [], 'Pablo Picasso': [], 'Frida Kahlo': [], 'Johann Sebastian Bach': [], 'Wolfgang Amadeus Mozart': [], 'Ludwig van Beethoven': [], 'Louis Armstrong': [], 'The Beatles': [], 'Michael Jackson': [], 'Hippocrates': [], 'Avicenna': [], 'Shen Kuo': [], 'Johannes Gutenberg': [], 'Nicolaus Copernicus': [], 'Galileo Galilei': [], 'Isaac Newton': [], 'Carl Linnaeus': [], 'Antoine Lavoisier': [], 'Michael Faraday': [], 'Charles Darwin': [], 'Florence Nightingale': [], 'Louis Pasteur': [], 'James Clerk Maxwell': [], 'Dmitri Mendeleev': [], 'Thomas Edison': [], 'Nikola Tesla': [], 'Marie Curie': [], 'Albert Einstein': [], 'Archimedes': [], 'Euclid': [], 'Muhammad ibn Musa al-Khwarizmi': [], 'Leonhard Euler': [], 'Carl Friedrich Gauss': [], 'Emmy Noether': [], 'Kurt GÃ¶del': [], 'Alan Turing': [], 'Charlie Chaplin': [], 'Walt Disney': [], 'Henry Ford': []}
>>> x = set(themes)
>>> page_lists = {theme:[] for theme in x}
>>> page_lists
{'Geography': [], 'Science': [], 'Technology': [], 'History': [], 'Health, medicine and disease': [], 'Everyday life': [], 'Arts': [], 'Philosophy and religion': [], 'Society and social sciences': [], 'Mathematics': [], 'People': []}
>>> for title, theme in zip(titles, themes):
	page_lists[theme].append(title)

	
>>> page_lists["Mathematics"]
['Mathematics', 'Algorithm', 'Mathematical proof', 'Set (mathematics)', 'Function (mathematics)', 'Combinatorics', 'Number', 'Real number', 'E (mathematical constant)', 'Pi', 'Fraction', 'Integer', '0', 'Natural number', 'Prime number', 'Complex number', 'Number theory', 'Algebra', 'Equation', 'Variable (mathematics)', 'Linear algebra', 'Abstract algebra', 'Mathematical analysis', 'Calculus', 'Infinity', 'Limit (mathematics)', 'Series (mathematics)', 'Arithmetic', 'Exponentiation', 'Logarithm', 'Nth root', 'Geometry', 'Angle', 'Trigonometry', 'Area', 'Conic section', 'Circle', 'Line (geometry)', 'Polygon', 'Triangle', 'Three-dimensional space', 'Volume', 'Topology', 'Probability', 'Statistics']
>>> [x for x in page_lists["People"] if "Kurt" in x]
['Kurt Gödel']
>>> thematic_word_counts = {theme:Counter() for theme in page_lists}
>>> for current_theme in thematic_word_counts:
	i = 0
	for article_name in page_lists[current_theme]:
		i += 1
		print(f"{current_theme} {i}/{len(page_lists[current_theme])}:", article_name)
		article_word_counts = word_counts(article_name)
		for word in article_word_counts:
			thematic_word_counts[current_theme][word] += article_word_counts[word]

			
Geography 1/106: Geography
Geography 2/106: Continent
Geography 3/106: Africa
Geography 4/106: Antarctica
Geography 5/106: Asia
Geography 6/106: Europe
Geography 7/106: North America
Geography 8/106: South America
Geography 9/106: Arctic
Geography 10/106: Caribbean
Geography 11/106: Middle East
Geography 12/106: Oceania
Geography 13/106: Land
Geography 14/106: Desert
Geography 15/106: Sahara
Geography 16/106: Forest
Geography 17/106: Amazon rainforest
Geography 18/106: Grassland
Geography 19/106: Island
Geography 20/106: Mountain
Geography 21/106: Alps
Geography 22/106: Andes
Geography 23/106: Himalayas
Geography 24/106: Rocky Mountains
Geography 25/106: Sea
Geography 26/106: Arctic Ocean
Geography 27/106: Atlantic Ocean
Geography 28/106: Mediterranean Sea
Geography 29/106: Indian Ocean
Geography 30/106: Pacific Ocean
Geography 31/106: Great Barrier Reef
Geography 32/106: Southern Ocean
Geography 33/106: Lake
Geography 34/106: Caspian Sea
Geography 35/106: Great Lakes
Geography 36/106: Lake Victoria
Geography 37/106: River
Geography 38/106: Amazon River
Geography 39/106: Ganges
Geography 40/106: Mississippi River
Geography 41/106: Nile
Geography 42/106: Yangtze
Geography 43/106: Glacier
Geography 44/106: Country
Geography 45/106: Algeria
Geography 46/106: Democratic Republic of the Congo
Geography 47/106: Egypt
Geography 48/106: Ethiopia
Geography 49/106: Kenya
Geography 50/106: Nigeria
Geography 51/106: South Africa
Geography 52/106: Tanzania
Geography 53/106: Bangladesh
Geography 54/106: China
Geography 55/106: India
Geography 56/106: Indonesia
Geography 57/106: Iran
Geography 58/106: Israel
Geography 59/106: Japan
Geography 60/106: Malaysia
Geography 61/106: Myanmar
Geography 62/106: Pakistan
Geography 63/106: Philippines
Geography 64/106: Saudi Arabia
Geography 65/106: South Korea
Geography 66/106: Taiwan
Geography 67/106: Thailand
Geography 68/106: United Arab Emirates
Geography 69/106: Vietnam
Geography 70/106: Russia
Geography 71/106: Turkey
Geography 72/106: France
Geography 73/106: Germany
Geography 74/106: Italy
Geography 75/106: Netherlands
Geography 76/106: Poland
Geography 77/106: Spain
Geography 78/106: Ukraine
Geography 79/106: United Kingdom
Geography 80/106: Canada
Geography 81/106: Mexico
Geography 82/106: United States
Geography 83/106: Australia
Geography 84/106: Argentina
Geography 85/106: Brazil
Geography 86/106: Colombia
Geography 87/106: City
Geography 88/106: Cairo
Geography 89/106: Lagos
Geography 90/106: Beijing
Geography 91/106: Hong Kong
Geography 92/106: Tokyo
Geography 93/106: Jakarta
Geography 94/106: Singapore
Geography 95/106: Delhi
Geography 96/106: Mumbai
Geography 97/106: Istanbul
Geography 98/106: Jerusalem
Geography 99/106: Mecca
Geography 100/106: London
Geography 101/106: Moscow
Geography 102/106: Paris
Geography 103/106: Rome
Geography 104/106: Mexico City
Geography 105/106: New York City
Geography 106/106: São Paulo
Science 1/210: Science
Science 2/210: Scientific method
Science 3/210: Measurement
Science 4/210: International System of Units
Science 5/210: Nature
Science 6/210: Astronomy
Science 7/210: Universe
Science 8/210: Solar System
Science 9/210: Sun
Science 10/210: Mercury (planet)
Science 11/210: Venus
Science 12/210: Earth
Science 13/210: Moon
Science 14/210: Mars
Science 15/210: Jupiter
Science 16/210: Saturn
Science 17/210: Uranus
Science 18/210: Neptune
Science 19/210: Asteroid
Science 20/210: Big Bang
Science 21/210: Black hole
Science 22/210: Comet
Science 23/210: Galaxy
Science 24/210: Milky Way
Science 25/210: Natural satellite
Science 26/210: Orbit
Science 27/210: Outer space
Science 28/210: Physical cosmology
Science 29/210: Planet
Science 30/210: Star
Science 31/210: Supernova
Science 32/210: Physics
Science 33/210: Energy
Science 34/210: Time
Science 35/210: Day
Science 36/210: Year
Science 37/210: Classical mechanics
Science 38/210: Mass
Science 39/210: Momentum
Science 40/210: Motion
Science 41/210: Newton's laws of motion
Science 42/210: Force
Science 43/210: Electromagnetism
Science 44/210: Gravity
Science 45/210: Strong interaction
Science 46/210: Weak interaction
Science 47/210: Magnetism
Science 48/210: Matter
Science 49/210: State of matter
Science 50/210: Atom
Science 51/210: Particle physics
Science 52/210: Standard Model
Science 53/210: Subatomic particle
Science 54/210: Electron
Science 55/210: Neutron
Science 56/210: Photon
Science 57/210: Proton
Science 58/210: Quantum mechanics
Science 59/210: Radioactive decay
Science 60/210: Space
Science 61/210: Vacuum
Science 62/210: Thermodynamics
Science 63/210: Heat
Science 64/210: Temperature
Science 65/210: Theory of relativity
Science 66/210: Speed of light
Science 67/210: Wave
Science 68/210: Electromagnetic radiation
Science 69/210: Light
Science 70/210: Color
Science 71/210: Optics
Science 72/210: Sound
Science 73/210: Biology
Science 74/210: Life
Science 75/210: Cell (biology)
Science 76/210: Death
Science 77/210: Suicide
Science 78/210: Abiogenesis
Science 79/210: Evolution
Science 80/210: Human evolution
Science 81/210: Natural selection
Science 82/210: Organism
Science 83/210: Archaea
Science 84/210: Bacteria
Science 85/210: Eukaryote
Science 86/210: Animal
Science 87/210: Zoology
Science 88/210: Amphibian
Science 89/210: Arthropod
Science 90/210: Crustacean
Science 91/210: Insect
Science 92/210: Bird
Science 93/210: Chicken
Science 94/210: Fish
Science 95/210: Mammal
Science 96/210: Cat
Science 97/210: Cattle
Science 98/210: Dog
Science 99/210: Horse
Science 100/210: Pig
Science 101/210: Primate
Science 102/210: Human
Science 103/210: Rodent
Science 104/210: Sheep
Science 105/210: Mollusca
Science 106/210: Reptile
Science 107/210: Dinosaur
Science 108/210: Plant
Science 109/210: Algae
Science 110/210: Botany
Science 111/210: Cotton
Science 112/210: Flower
Science 113/210: Seed
Science 114/210: Tree
Science 115/210: Fungus
Science 116/210: Virus
Science 117/210: Anatomy
Science 118/210: Human body
Science 119/210: Circulatory system
Science 120/210: Blood
Science 121/210: Heart
Science 122/210: Lung
Science 123/210: Digestion
Science 124/210: Liver
Science 125/210: Immune system
Science 126/210: Skeletal muscle
Science 127/210: Nervous system
Science 128/210: Brain
Science 129/210: Ear
Science 130/210: Eye
Science 131/210: Sense
Science 132/210: Skeleton
Science 133/210: Bone
Science 134/210: Skin
Science 135/210: Ecology
Science 136/210: Biodiversity
Science 137/210: Ecosystem
Science 138/210: Extinction
Science 139/210: Genetics
Science 140/210: DNA
Science 141/210: Gene
Science 142/210: Heredity
Science 143/210: RNA
Science 144/210: Metabolism
Science 145/210: Molecular biology
Science 146/210: Hormone
Science 147/210: Protein
Science 148/210: Paleontology
Science 149/210: Photosynthesis
Science 150/210: Reproduction
Science 151/210: Sex
Science 152/210: Pregnancy
Science 153/210: Sleep
Science 154/210: Taxonomy (biology)
Science 155/210: Species
Science 156/210: Chemistry
Science 157/210: Biochemistry
Science 158/210: Inorganic chemistry
Science 159/210: Organic chemistry
Science 160/210: Physical chemistry
Science 161/210: Chemical element
Science 162/210: Periodic table
Science 163/210: Aluminium
Science 164/210: Carbon
Science 165/210: Copper
Science 166/210: Gold
Science 167/210: Hydrogen
Science 168/210: Iron
Science 169/210: Nitrogen
Science 170/210: Oxygen
Science 171/210: Phosphorus
Science 172/210: Silicon
Science 173/210: Silver
Science 174/210: Sulfur
Science 175/210: Chemical compound
Science 176/210: Water
Science 177/210: Carbon dioxide
Science 178/210: Chemical bond
Science 179/210: Molecule
Science 180/210: Chemical reaction
Science 181/210: Acid-base reaction
Science 182/210: Catalysis
Science 183/210: Redox
Science 184/210: Metal
Science 185/210: Alloy
Science 186/210: Bronze
Science 187/210: Steel
Science 188/210: Earth science
Science 189/210: History of Earth
Science 190/210: Atmosphere of Earth
Science 191/210: Internal structure of Earth
Science 192/210: Season
Science 193/210: Flood
Science 194/210: Climate
Science 195/210: Climate change
Science 196/210: Weather
Science 197/210: Cloud
Science 198/210: Rain
Science 199/210: Snow
Science 200/210: Tornado
Science 201/210: Tropical cyclone
Science 202/210: Wind
Science 203/210: Geology
Science 204/210: Earthquake
Science 205/210: Erosion
Science 206/210: Mineral
Science 207/210: Plate tectonics
Science 208/210: Rock (geology)
Science 209/210: Soil
Science 210/210: Volcano
Technology 1/98: Technology
Technology 2/98: Engineering
Technology 3/98: Civil engineering
Technology 4/98: Mechanical engineering
Technology 5/98: Electricity
Technology 6/98: Electric battery
Technology 7/98: Fire
Technology 8/98: Explosive
Technology 9/98: Gunpowder
Technology 10/98: Fossil fuel
Technology 11/98: Coal
Technology 12/98: Natural gas
Technology 13/98: Petroleum
Technology 14/98: Nuclear power
Technology 15/98: Renewable energy
Technology 16/98: Hydropower
Technology 17/98: Solar energy
Technology 18/98: Wind power
Technology 19/98: Animal husbandry
Technology 20/98: Domestication
Technology 21/98: Biotechnology
Technology 22/98: Genetic engineering
Technology 23/98: Fertilizer
Technology 24/98: Food preservation
Technology 25/98: Garden
Technology 26/98: Medical imaging
Technology 27/98: Refrigeration
Technology 28/98: Stove
Technology 29/98: Weapon
Technology 30/98: Armour
Technology 31/98: Bow and arrow
Technology 32/98: Firearm
Technology 33/98: Knife
Technology 34/98: Nuclear weapon
Technology 35/98: Tool
Technology 36/98: Simple machine
Technology 37/98: Wheel
Technology 38/98: Engine
Technology 39/98: Electric motor
Technology 40/98: Internal combustion engine
Technology 41/98: Jet engine
Technology 42/98: Steam engine
Technology 43/98: Robotics
Technology 44/98: Printing
Technology 45/98: Book
Technology 46/98: Mail
Technology 47/98: Telecommunications
Technology 48/98: Internet
Technology 49/98: Radio
Technology 50/98: Telephone
Technology 51/98: Mobile phone
Technology 52/98: Video
Technology 53/98: Television
Technology 54/98: Computer science
Technology 55/98: Computer
Technology 56/98: Artificial intelligence
Technology 57/98: Cryptography
Technology 58/98: Electronics
Technology 59/98: Electric light
Technology 60/98: Integrated circuit
Technology 61/98: Semiconductor device
Technology 62/98: Rocket
Technology 63/98: Satellite
Technology 64/98: Space exploration
Technology 65/98: Spaceflight
Technology 66/98: Space station
Technology 67/98: Transport
Technology 68/98: Aircraft
Technology 69/98: Bicycle
Technology 70/98: Car
Technology 71/98: Rail transport
Technology 72/98: Ship
Technology 73/98: Navigation
Technology 74/98: Compass
Technology 75/98: Map
Technology 76/98: Radar
Technology 77/98: Calendar
Technology 78/98: Clock
Technology 79/98: Fortification
Technology 80/98: Infrastructure
Technology 81/98: Bridge
Technology 82/98: Canal
Technology 83/98: Dam
Technology 84/98: Road
Technology 85/98: Concrete
Technology 86/98: Glass
Technology 87/98: Masonry
Technology 88/98: Metallurgy
Technology 89/98: Natural rubber
Technology 90/98: Paper
Technology 91/98: Plastic
Technology 92/98: Textile
Technology 93/98: Wood
Technology 94/98: Camera
Technology 95/98: Laser
Technology 96/98: Lens
Technology 97/98: Microscope
Technology 98/98: Telescope
History 1/83: History
History 2/83: Human history
History 3/83: Civilization
History 4/83: Archaeology
History 5/83: History of Africa
History 6/83: History of Asia
History 7/83: History of East Asia
History 8/83: History of India
History 9/83: History of the Middle East
History 10/83: History of Europe
History 11/83: History of North America
History 12/83: History of Oceania
History 13/83: History of South America
History 14/83: History of science
History 15/83: History of art
History 16/83: History of agriculture
History 17/83: History of architecture
History 18/83: History of film
History 19/83: History of literature
History 20/83: History of mathematics
History 21/83: History of medicine
History 22/83: History of music
History 23/83: History of technology
History 24/83: Military history
History 25/83: Prehistory
History 26/83: Stone Age
History 27/83: Early human migrations
History 28/83: Neolithic Revolution
History 29/83: Ancient history
History 30/83: Bronze Age
History 31/83: Ancient Egypt
History 32/83: Indus Valley Civilisation
History 33/83: Mesopotamia
History 34/83: Sumer
History 35/83: Phoenicia
History 36/83: Iron Age
History 37/83: Ancient Greece
History 38/83: Ancient Rome
History 39/83: Achaemenid Empire
History 40/83: Gupta Empire
History 41/83: Han dynasty
History 42/83: Silk Road
History 43/83: Pre-Columbian era
History 44/83: Andean civilizations
History 45/83: Mesoamerica
History 46/83: Maya civilization
History 47/83: Post-classical history
History 48/83: Aztecs
History 49/83: Inca Empire
History 50/83: Islamic Golden Age
History 51/83: Middle Ages
History 52/83: Black Death
History 53/83: Byzantine Empire
History 54/83: Crusades
History 55/83: Holy Roman Empire
History 56/83: Viking Age
History 57/83: Mongol Empire
History 58/83: Ottoman Empire
History 59/83: Tang dynasty
History 60/83: Early modern period
History 61/83: Renaissance
History 62/83: Age of Discovery
History 63/83: European colonization of the Americas
History 64/83: Western imperialism in Asia
History 65/83: Spanish Empire
History 66/83: Reformation
History 67/83: Mughal Empire
History 68/83: Scientific Revolution
History 69/83: Age of Enlightenment
History 70/83: Late modern period
History 71/83: British Empire
History 72/83: American Revolution
History 73/83: French Revolution
History 74/83: Industrial Revolution
History 75/83: Scramble for Africa
History 76/83: World War I
History 77/83: Soviet Union
History 78/83: Great Depression
History 79/83: World War II
History 80/83: Decolonization
History 81/83: Cold War
History 82/83: Green Revolution
History 83/83: Information Age
Health, medicine and disease 1/41: Disease
Health, medicine and disease 2/41: Allergy
Health, medicine and disease 3/41: Asthma
Health, medicine and disease 4/41: Cancer
Health, medicine and disease 5/41: Cardiovascular disease
Health, medicine and disease 6/41: Stroke
Health, medicine and disease 7/41: Diabetes
Health, medicine and disease 8/41: Gastroenteritis
Health, medicine and disease 9/41: Infection
Health, medicine and disease 10/41: Common cold
Health, medicine and disease 11/41: Influenza
Health, medicine and disease 12/41: Malaria
Health, medicine and disease 13/41: Pneumonia
Health, medicine and disease 14/41: Sexually transmitted infection
Health, medicine and disease 15/41: HIV_AIDS
Health, medicine and disease 16/41: Smallpox
Health, medicine and disease 17/41: Tuberculosis
Health, medicine and disease 18/41: Mental disorder
Health, medicine and disease 19/41: Injury
Health, medicine and disease 20/41: Medicine
Health, medicine and disease 21/41: Dentistry
Health, medicine and disease 22/41: Hospital
Health, medicine and disease 23/41: Nursing
Health, medicine and disease 24/41: Surgery
Health, medicine and disease 25/41: Ageing
Health, medicine and disease 26/41: Exercise
Health, medicine and disease 27/41: Health
Health, medicine and disease 28/41: Mental health
Health, medicine and disease 29/41: Hygiene
Health, medicine and disease 30/41: Sanitation
Health, medicine and disease 31/41: Nutrition
Health, medicine and disease 32/41: Obesity
Health, medicine and disease 33/41: Drug
Health, medicine and disease 34/41: Medication
Health, medicine and disease 35/41: Anesthesia
Health, medicine and disease 36/41: Antibiotic
Health, medicine and disease 37/41: Birth control
Health, medicine and disease 38/41: Vaccine
Health, medicine and disease 39/41: Addiction
Health, medicine and disease 40/41: Alcoholism
Health, medicine and disease 41/41: Smoking
Everyday life 1/57: Clothing
Everyday life 2/57: Home
Everyday life 3/57: Furniture
Everyday life 4/57: Jewellery
Everyday life 5/57: Ethnic group
Everyday life 6/57: Family
Everyday life 7/57: Adult
Everyday life 8/57: Adolescence
Everyday life 9/57: Child
Everyday life 10/57: Infant
Everyday life 11/57: Marriage
Everyday life 12/57: Old age
Everyday life 13/57: Parenting
Everyday life 14/57: Friendship
Everyday life 15/57: Human sexuality
Everyday life 16/57: Sexual intercourse
Everyday life 17/57: Sexual orientation
Everyday life 18/57: Gender
Everyday life 19/57: Man
Everyday life 20/57: Woman
Everyday life 21/57: Cooking
Everyday life 22/57: Food
Everyday life 23/57: Bread
Everyday life 24/57: Cereal
Everyday life 25/57: Wheat
Everyday life 26/57: Maize
Everyday life 27/57: Rice
Everyday life 28/57: Cheese
Everyday life 29/57: Fruit
Everyday life 30/57: Meat
Everyday life 31/57: Salt
Everyday life 32/57: Spice
Everyday life 33/57: Sugar
Everyday life 34/57: Vegetable
Everyday life 35/57: Potato
Everyday life 36/57: Soybean
Everyday life 37/57: Drink
Everyday life 38/57: Alcoholic beverage
Everyday life 39/57: Coffee
Everyday life 40/57: Drinking water
Everyday life 41/57: Milk
Everyday life 42/57: Tea
Everyday life 43/57: Entertainment
Everyday life 44/57: Play (activity)
Everyday life 45/57: Game
Everyday life 46/57: Board game
Everyday life 47/57: Card game
Everyday life 48/57: Gambling
Everyday life 49/57: Video game
Everyday life 50/57: Sport
Everyday life 51/57: Association football
Everyday life 52/57: Sport of athletics
Everyday life 53/57: Olympic Games
Everyday life 54/57: Toy
Everyday life 55/57: Martial arts
Everyday life 56/57: Swimming
Everyday life 57/57: Tourism
Arts 1/45: The arts
Arts 2/45: Art
Arts 3/45: Prehistoric art
Arts 4/45: Fashion
Arts 5/45: Museum
Arts 6/45: Abstract art
Arts 7/45: Modernism
Arts 8/45: Realism (arts)
Arts 9/45: Romanticism
Arts 10/45: Architecture
Arts 11/45: Great Pyramid of Giza
Arts 12/45: Great Wall of China
Arts 13/45: Literature
Arts 14/45: English literature
Arts 15/45: Fiction
Arts 16/45: Novel
Arts 17/45: Short story
Arts 18/45: Fairy tale
Arts 19/45: Poetry
Arts 20/45: Epic poetry
Arts 21/45: Music
Arts 22/45: Musical instrument
Arts 23/45: Piano
Arts 24/45: Singing
Arts 25/45: Classical music
Arts 26/45: Folk music
Arts 27/45: Jazz
Arts 28/45: Pop music
Arts 29/45: Rock music
Arts 30/45: Performing arts
Arts 31/45: Dance
Arts 32/45: Opera
Arts 33/45: Orchestra
Arts 34/45: Theatre
Arts 35/45: Visual arts
Arts 36/45: Film
Arts 37/45: Animation
Arts 38/45: Calligraphy
Arts 39/45: Comics
Arts 40/45: Design
Arts 41/45: Drawing
Arts 42/45: Painting
Arts 43/45: Photography
Arts 44/45: Pottery
Arts 45/45: Sculpture
Philosophy and religion 1/55: Philosophy
Philosophy and religion 2/55: Philosophy of science
Philosophy and religion 3/55: Aesthetics
Philosophy and religion 4/55: Epistemology
Philosophy and religion 5/55: Knowledge
Philosophy and religion 6/55: Belief
Philosophy and religion 7/55: Reason
Philosophy and religion 8/55: Truth
Philosophy and religion 9/55: Ethics
Philosophy and religion 10/55: Good and evil
Philosophy and religion 11/55: Logic
Philosophy and religion 12/55: Metaphysics
Philosophy and religion 13/55: Free will
Philosophy and religion 14/55: Ontology
Philosophy and religion 15/55: Eastern philosophy
Philosophy and religion 16/55: Confucianism
Philosophy and religion 17/55: Western philosophy
Philosophy and religion 18/55: Myth
Philosophy and religion 19/55: Greek mythology
Philosophy and religion 20/55: Religion
Philosophy and religion 21/55: Afterlife
Philosophy and religion 22/55: Deity
Philosophy and religion 23/55: God
Philosophy and religion 24/55: Meditation
Philosophy and religion 25/55: New religious movement
Philosophy and religion 26/55: Prayer
Philosophy and religion 27/55: Ritual
Philosophy and religion 28/55: Shamanism
Philosophy and religion 29/55: Soul
Philosophy and religion 30/55: Spirituality
Philosophy and religion 31/55: Secularism
Philosophy and religion 32/55: Atheism
Philosophy and religion 33/55: Christianity
Philosophy and religion 34/55: Bible
Philosophy and religion 35/55: Catholic Church
Philosophy and religion 36/55: Eastern Orthodox Church
Philosophy and religion 37/55: Protestantism
Philosophy and religion 38/55: Islam
Philosophy and religion 39/55: Shia Islam
Philosophy and religion 40/55: Sunni Islam
Philosophy and religion 41/55: Quran
Philosophy and religion 42/55: Judaism
Philosophy and religion 43/55: Talmud
Philosophy and religion 44/55: Chinese folk religion
Philosophy and religion 45/55: Shinto
Philosophy and religion 46/55: Taoism
Philosophy and religion 47/55: Buddhism
Philosophy and religion 48/55: Mahayana
Philosophy and religion 49/55: Theravada
Philosophy and religion 50/55: Hinduism
Philosophy and religion 51/55: Vedas
Philosophy and religion 52/55: Bhagavad Gita
Philosophy and religion 53/55: Jainism
Philosophy and religion 54/55: Sikhism
Philosophy and religion 55/55: Traditional African religions
Society and social sciences 1/146: Culture
Society and social sciences 2/146: Folklore
Society and social sciences 3/146: Festival
Society and social sciences 4/146: Oral tradition
Society and social sciences 5/146: Popular culture
Society and social sciences 6/146: Society
Society and social sciences 7/146: Community
Society and social sciences 8/146: Power (social and political)
Society and social sciences 9/146: Social class
Society and social sciences 10/146: Communication
Society and social sciences 11/146: Social science
Society and social sciences 12/146: Anthropology
Society and social sciences 13/146: Sociology
Society and social sciences 14/146: Politics
Society and social sciences 15/146: Political party
Society and social sciences 16/146: Political science
Society and social sciences 17/146: Colonialism
Society and social sciences 18/146: Imperialism
Society and social sciences 19/146: Government
Society and social sciences 20/146: Democracy
Society and social sciences 21/146: Dictatorship
Society and social sciences 22/146: Monarchy
Society and social sciences 23/146: Ideology
Society and social sciences 24/146: Anarchism
Society and social sciences 25/146: Capitalism
Society and social sciences 26/146: Communism
Society and social sciences 27/146: Conservatism
Society and social sciences 28/146: Fascism
Society and social sciences 29/146: Liberalism
Society and social sciences 30/146: Nationalism
Society and social sciences 31/146: Socialism
Society and social sciences 32/146: State (polity)
Society and social sciences 33/146: Diplomacy
Society and social sciences 34/146: Military
Society and social sciences 35/146: European Union
Society and social sciences 36/146: International Red Cross and Red Crescent Movement
Society and social sciences 37/146: NATO
Society and social sciences 38/146: United Nations
Society and social sciences 39/146: War
Society and social sciences 40/146: Genocide
Society and social sciences 41/146: Peace
Society and social sciences 42/146: Terrorism
Society and social sciences 43/146: Education
Society and social sciences 44/146: School
Society and social sciences 45/146: Library
Society and social sciences 46/146: University
Society and social sciences 47/146: Business
Society and social sciences 48/146: Corporation
Society and social sciences 49/146: Management
Society and social sciences 50/146: Marketing
Society and social sciences 51/146: Retail
Society and social sciences 52/146: Trade union
Society and social sciences 53/146: Economics
Society and social sciences 54/146: Trade
Society and social sciences 55/146: Supply and demand
Society and social sciences 56/146: Employment
Society and social sciences 57/146: Finance
Society and social sciences 58/146: Bank
Society and social sciences 59/146: Money
Society and social sciences 60/146: Insurance
Society and social sciences 61/146: Tax
Society and social sciences 62/146: Economy
Society and social sciences 63/146: Agriculture
Society and social sciences 64/146: Manufacturing
Society and social sciences 65/146: Construction
Society and social sciences 66/146: Fishing
Society and social sciences 67/146: Hunting
Society and social sciences 68/146: Mining
Society and social sciences 69/146: Abortion
Society and social sciences 70/146: Disability
Society and social sciences 71/146: Discrimination
Society and social sciences 72/146: Racism
Society and social sciences 73/146: Sexism
Society and social sciences 74/146: Environmentalism
Society and social sciences 75/146: Pollution
Society and social sciences 76/146: Famine
Society and social sciences 77/146: Feminism
Society and social sciences 78/146: Globalization
Society and social sciences 79/146: Human migration
Society and social sciences 80/146: Human rights
Society and social sciences 81/146: Liberty
Society and social sciences 82/146: Privacy
Society and social sciences 83/146: Slavery
Society and social sciences 84/146: Social equality
Society and social sciences 85/146: Suffrage
Society and social sciences 86/146: Indigenous peoples
Society and social sciences 87/146: Poverty
Society and social sciences 88/146: Violence
Society and social sciences 89/146: Welfare
Society and social sciences 90/146: Law
Society and social sciences 91/146: Crime
Society and social sciences 92/146: Constitution
Society and social sciences 93/146: Justice
Society and social sciences 94/146: Police
Society and social sciences 95/146: Property
Society and social sciences 96/146: Psychology
Society and social sciences 97/146: Emotion
Society and social sciences 98/146: Anger
Society and social sciences 99/146: Fear
Society and social sciences 100/146: Happiness
Society and social sciences 101/146: Humour
Society and social sciences 102/146: Love
Society and social sciences 103/146: Mind
Society and social sciences 104/146: Consciousness
Society and social sciences 105/146: Dream
Society and social sciences 106/146: Memory
Society and social sciences 107/146: Thought
Society and social sciences 108/146: Human behavior
Society and social sciences 109/146: Intelligence
Society and social sciences 110/146: Learning
Society and social sciences 111/146: Personality
Society and social sciences 112/146: Language
Society and social sciences 113/146: Indo-European languages
Society and social sciences 114/146: Bengali language
Society and social sciences 115/146: English language
Society and social sciences 116/146: French language
Society and social sciences 117/146: German language
Society and social sciences 118/146: Greek language
Society and social sciences 119/146: Hindustani language
Society and social sciences 120/146: Latin
Society and social sciences 121/146: Portuguese language
Society and social sciences 122/146: Russian language
Society and social sciences 123/146: Spanish language
Society and social sciences 124/146: Arabic
Society and social sciences 125/146: Chinese language
Society and social sciences 126/146: Japanese language
Society and social sciences 127/146: Malay language
Society and social sciences 128/146: Swahili language
Society and social sciences 129/146: Linguistics
Society and social sciences 130/146: Grammar
Society and social sciences 131/146: Word
Society and social sciences 132/146: Personal name
Society and social sciences 133/146: Speech
Society and social sciences 134/146: Writing
Society and social sciences 135/146: Alphabet
Society and social sciences 136/146: Arabic script
Society and social sciences 137/146: Brahmic scripts
Society and social sciences 138/146: Cyrillic script
Society and social sciences 139/146: Greek alphabet
Society and social sciences 140/146: Latin script
Society and social sciences 141/146: Arabic numerals
Society and social sciences 142/146: Chinese characters
Society and social sciences 143/146: Mass media
Society and social sciences 144/146: Broadcasting
Society and social sciences 145/146: News
Society and social sciences 146/146: Publishing
Mathematics 1/45: Mathematics
Mathematics 2/45: Algorithm
Mathematics 3/45: Mathematical proof
Mathematics 4/45: Set (mathematics)
Mathematics 5/45: Function (mathematics)
Mathematics 6/45: Combinatorics
Mathematics 7/45: Number
Mathematics 8/45: Real number
Mathematics 9/45: E (mathematical constant)
Mathematics 10/45: Pi
Mathematics 11/45: Fraction
Mathematics 12/45: Integer
Mathematics 13/45: 0
Mathematics 14/45: Natural number
Mathematics 15/45: Prime number
Mathematics 16/45: Complex number
Mathematics 17/45: Number theory
Mathematics 18/45: Algebra
Mathematics 19/45: Equation
Mathematics 20/45: Variable (mathematics)
Mathematics 21/45: Linear algebra
Mathematics 22/45: Abstract algebra
Mathematics 23/45: Mathematical analysis
Mathematics 24/45: Calculus
Mathematics 25/45: Infinity
Mathematics 26/45: Limit (mathematics)
Mathematics 27/45: Series (mathematics)
Mathematics 28/45: Arithmetic
Mathematics 29/45: Exponentiation
Mathematics 30/45: Logarithm
Mathematics 31/45: Nth root
Mathematics 32/45: Geometry
Mathematics 33/45: Angle
Mathematics 34/45: Trigonometry
Mathematics 35/45: Area
Mathematics 36/45: Conic section
Mathematics 37/45: Circle
Mathematics 38/45: Line (geometry)
Mathematics 39/45: Polygon
Mathematics 40/45: Triangle
Mathematics 41/45: Three-dimensional space
Mathematics 42/45: Volume
Mathematics 43/45: Topology
Mathematics 44/45: Probability
Mathematics 45/45: Statistics
People 1/112: Hammurabi
People 2/112: Hatshepsut
People 3/112: Ramesses II
People 4/112: Cyrus the Great
People 5/112: Alexander the Great
People 6/112: Ashoka
People 7/112: Qin Shi Huang
People 8/112: Julius Caesar
People 9/112: Augustus
People 10/112: Charlemagne
People 11/112: Genghis Khan
People 12/112: Mansa Musa
People 13/112: Joan of Arc
People 14/112: Suleiman the Magnificent
People 15/112: Akbar
People 16/112: Elizabeth I
People 17/112: Catherine the Great
People 18/112: George Washington
People 19/112: Napoleon
People 20/112: Simón Bolívar
People 21/112: Abraham Lincoln
People 22/112: Mahatma Gandhi
People 23/112: Joseph Stalin
People 24/112: Adolf Hitler
People 25/112: Mao Zedong
People 26/112: Nelson Mandela
People 27/112: Abraham
People 28/112: Moses
People 29/112: Gautama Buddha
People 30/112: Jesus
People 31/112: Paul the Apostle
People 32/112: Muhammad
People 33/112: Adi Shankara
People 34/112: Martin Luther
People 35/112: Marco Polo
People 36/112: Zheng He
People 37/112: Christopher Columbus
People 38/112: Vasco da Gama
People 39/112: Ferdinand Magellan
People 40/112: James Cook
People 41/112: Roald Amundsen
People 42/112: Confucius
People 43/112: Laozi
People 44/112: Herodotus
People 45/112: Socrates
People 46/112: Plato
People 47/112: Aristotle
People 48/112: Cicero
People 49/112: Thomas Aquinas
People 50/112: Ibn Khaldun
People 51/112: Niccolò Machiavelli
People 52/112: René Descartes
People 53/112: John Locke
People 54/112: Adam Smith
People 55/112: Immanuel Kant
People 56/112: Mary Wollstonecraft
People 57/112: Karl Marx
People 58/112: Friedrich Nietzsche
People 59/112: Sigmund Freud
People 60/112: Homer
People 61/112: Virgil
People 62/112: Li Bai
People 63/112: Murasaki Shikibu
People 64/112: Rumi
People 65/112: Dante Alighieri
People 66/112: Miguel de Cervantes
People 67/112: William Shakespeare
People 68/112: Voltaire
People 69/112: Leo Tolstoy
People 70/112: Rabindranath Tagore
People 71/112: Leonardo da Vinci
People 72/112: Michelangelo
People 73/112: Rembrandt
People 74/112: Hokusai
People 75/112: Pablo Picasso
People 76/112: Frida Kahlo
People 77/112: Johann Sebastian Bach
People 78/112: Wolfgang Amadeus Mozart
People 79/112: Ludwig van Beethoven
People 80/112: Louis Armstrong
People 81/112: The Beatles
People 82/112: Michael Jackson
People 83/112: Hippocrates
People 84/112: Avicenna
People 85/112: Shen Kuo
People 86/112: Johannes Gutenberg
People 87/112: Nicolaus Copernicus
People 88/112: Galileo Galilei
People 89/112: Isaac Newton
People 90/112: Carl Linnaeus
People 91/112: Antoine Lavoisier
People 92/112: Michael Faraday
People 93/112: Charles Darwin
People 94/112: Florence Nightingale
People 95/112: Louis Pasteur
People 96/112: James Clerk Maxwell
People 97/112: Dmitri Mendeleev
People 98/112: Thomas Edison
People 99/112: Nikola Tesla
People 100/112: Marie Curie
People 101/112: Albert Einstein
People 102/112: Archimedes
People 103/112: Euclid
People 104/112: Muhammad ibn Musa al-Khwarizmi
People 105/112: Leonhard Euler
People 106/112: Carl Friedrich Gauss
People 107/112: Emmy Noether
People 108/112: Kurt Gödel
People 109/112: Alan Turing
People 110/112: Charlie Chaplin
People 111/112: Walt Disney
People 112/112: Henry Ford
>>> clipboard.copy(str(article_word_counts))
>>> clipboard.copy(str(thematic_word_counts))
>>> thematic_article_word_counts = thematic_word_counts
>>> del thematic_word_counts
>>> [(theme, thematic_article_word_counts[theme]["the"]) for theme in thematic_article_word_counts]
[('Geography', 96720), ('Science', 93392), ('Technology', 34709), ('History', 80022), ('Health, medicine and disease', 13964), ('Everyday life', 19664), ('Arts', 21609), ('Philosophy and religion', 36637), ('Society and social sciences', 66657), ('Mathematics', 15402), ('People', 65945)]
>>> [(theme, thematic_article_word_counts[theme]["god"]) for theme in thematic_article_word_counts]
[('Geography', 59), ('Science', 112), ('Technology', 2), ('History', 114), ('Health, medicine and disease', 5), ('Everyday life', 44), ('Arts', 8), ('Philosophy and religion', 1184), ('Society and social sciences', 154), ('Mathematics', 3), ('People', 584)]
>>> total_word_count = Counter()
>>> for theme in thematic_article_word_counts:
	for word in thematic_article_word_counts[theme]:
		total_word_count[word] += thematic_article_word_counts[theme][word]

		
>>> total_word_count["the"]
544721
>>> [(theme, thematic_article_word_counts[theme]["dinosaur"]) for theme in thematic_article_word_counts]
[('Geography', 5), ('Science', 105), ('Technology', 1), ('History', 0), ('Health, medicine and disease', 1), ('Everyday life', 0), ('Arts', 1), ('Philosophy and religion', 0), ('Society and social sciences', 2), ('Mathematics', 0), ('People', 0)]
>>> total_word_count["dinosaur"]
115
>>> total_number_of_words = sum(total_word_count.values())
>>> total_number_of_words
7724353
>>> relative_frequencies = {theme:{} for theme in hematic_article_word_counts}
Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    relative_frequencies = {theme:{} for theme in hematic_article_word_counts}
NameError: name 'hematic_article_word_counts' is not defined
>>> total_words_per_theme = {theme: sum(thematic_article_word_counts[theme].values()) for theme in thematic_article_word_counts}
>>> total_words_per_theme
{'Geography': 1133257, 'Science': 1388414, 'Technology': 567738, 'History': 927327, 'Health, medicine and disease': 273006, 'Everyday life': 356101, 'Arts': 319126, 'Philosophy and religion': 511266, 'Society and social sciences': 1040496, 'Mathematics': 221538, 'People': 986084}
>>> relative_frequencies = {theme:{thematic_article_word_counts[theme][word]/total_words_per_theme[theme]*total_word_count[word]/total_number_of_frequencies for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}
Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    relative_frequencies = {theme:{thematic_article_word_counts[theme][word]/total_words_per_theme[theme]*total_word_count[word]/total_number_of_frequencies for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}
  File "<pyshell#333>", line 1, in <dictcomp>
    relative_frequencies = {theme:{thematic_article_word_counts[theme][word]/total_words_per_theme[theme]*total_word_count[word]/total_number_of_frequencies for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}
  File "<pyshell#333>", line 1, in <setcomp>
    relative_frequencies = {theme:{thematic_article_word_counts[theme][word]/total_words_per_theme[theme]*total_word_count[word]/total_number_of_frequencies for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}
NameError: name 'total_number_of_frequencies' is not defined
>>> relative_frequencies = {theme:{thematic_article_word_counts[theme][word]/total_words_per_theme[theme]*total_word_count[word]/total_number_of_words for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}
>>> relative_frequencies["Mathematics"]["number"]
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    relative_frequencies["Mathematics"]["number"]
TypeError: 'set' object is not subscriptable
>>> type(relative_frequencies["Mathematics"])
<class 'set'>
>>> relative_frequencies = {theme: {word: thematic_article_word_counts[theme][word]/total_words_per_theme[theme]*total_word_count[word]/total_number_of_words for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}

>>> type(relative_frequencies["Mathematics"])
<class 'dict'>
>>> relative_frequencies["Mathematics"]["number"]
4.057318243683596e-06
>>> relative_frequencies["Mathematics"]["God"]
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    relative_frequencies["Mathematics"]["God"]
KeyError: 'God'
>>> relative_frequencies["Geography"]["number"]
5.614250947941907e-07
>>> relative_frequencies = {theme: {word: (thematic_article_word_counts[theme][word], total_words_per_theme[theme], total_word_count[word], total_number_of_words) for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}

>>> relative_frequencies["Mathematics"]["number"]
(1174, 221538, 5914, 7724353)
>>> 1174/221539
0.005299292675330303
>>> 1/0.005299292675330303
188.70442930153322
>>> total_number_of_words
7724353
>>> total_number_of_words/998
7739.832665330661
>>> thematic_article_word_counts["Mathematics"]["number"]
1174
>>> 5914/7724353
0.000765630467690951
>>> 0.005299292675330303/0.000765630467690951
6.921475697424019
>>> relative_frequencies = {theme: {word: (thematic_article_word_counts[theme][word]/total_words_per_theme[theme]) / (total_word_count[word]/total_number_of_words) for word in thematic_article_word_counts[theme]} for theme in thematic_article_word_counts}
>>> relative_frequencies["Mathematics"]["number"]
6.921506940261354
>>> relative_frequencies["Geography"]["number"]
0.9577527461900317
>>> for theme in relative_frequencies:
	print(theme, '\t', relative_frequencies[theme]["number"])

	
Geography 	 0.9577527461900317
Science 	 1.1034681956608137
Technology 	 0.8489052023981497
History 	 0.6155017960814095
Health, medicine and disease 	 1.1051483522156216
Everyday life 	 0.8986150410829334
Arts 	 0.6016389415052493
Philosophy and religion 	 0.5824635154318056
Society and social sciences 	 0.8749296927816747
Mathematics 	 6.921506940261354
People 	 0.5059763796769946
>>> for theme in relative_frequencies:
	print(theme, '\t', relative_frequencies[theme]["darwin"])

	
Geography 	 0.1968538532920746
Science 	 1.5866840303393936
Technology 	 0.34382101659161357
History 	 0.27063997718468635
Traceback (most recent call last):
  File "<pyshell#358>", line 2, in <module>
    print(theme, '\t', relative_frequencies[theme]["darwin"])
KeyError: 'darwin'
>>> for theme in relative_frequencies:
	print(theme, '\t', relative_frequencies[theme].get("darwin",0))

	
Geography 	 0.1968538532920746
Science 	 1.5866840303393936
Technology 	 0.34382101659161357
History 	 0.27063997718468635
Health, medicine and disease 	 0
Everyday life 	 0
Arts 	 0.3495265306183397
Philosophy and religion 	 0.10908509817796244
Society and social sciences 	 0.3484057235518944
Mathematics 	 0
People 	 4.383289242997246
>>> for theme in relative_frequencies:
	print(theme, '\t', relative_frequencies[theme].get("king",0))

	
Geography 	 1.139699125056043
Science 	 0.09633656121519252
Technology 	 0.14724554977717527
History 	 2.663880395921925
Health, medicine and disease 	 0.06124179976952444
Everyday life 	 0.2699695536668053
Arts 	 0.707280552622988
Philosophy and religion 	 0.6376874002253942
Society and social sciences 	 0.542317350658637
Mathematics 	 0
People 	 2.551777036820147
>>> for theme in relative_frequencies:
	print(theme, '\t', relative_frequencies[theme].get("god",0))

	
Geography 	 0.17723570539623046
Science 	 0.27461651738204723
Technology 	 0.011992497839939177
History 	 0.4185039517916863
Health, medicine and disease 	 0.062348416689114776
Everyday life 	 0.4206366403080321
Arts 	 0.08534054559830773
Philosophy and religion 	 7.883742062412954
Society and social sciences 	 0.5038577263883349
Mathematics 	 0.046099969792889176
People 	 2.016167230871006
>>> L = sorted(thematic_article_word_counts["Mathematics"].keys())
>>> L[0]
''
>>> L[-1]
'𝜆-terms'
>>> L[2000]
'3}{4}}}of57{\\displaystyle'
>>> L[20000]
'units'
>>> L[10000]
'germain).in'
>>> L[9000]
'factorizations21=3⋅7=(1+2−5)(1−2−5){\\displaystyle'
>>> L[5000]
'bolter'
>>> L = sorted(thematic_article_word_counts["Mathematics"].keys(), key = lambda word: thematic_article_word_counts["Mathematics"][word])
>>> L[0]
'formulas.until'
>>> L[1]
'tattonieren'
>>> len(L)
21946
>>> L[-1]
'the'
>>> L[-20:]
['number', 'this', 'numbers', 'or', 'with', 'an', 'by', '', 'be', 'are', 'for', 'as', 'that', 'to', 'in', 'and', 'is', 'a', 'of', 'the']
>>> L = sorted(thematic_article_word_counts["Mathematics"].keys(), key = lambda word: relative_frequencies["Mathematics"][word])
>>> L[0]
'political'
>>> L[1]
'empire'
>>> L[2]
'her'
>>> L[3]
'war'
>>> for theme in relative_frequencies:
	print(theme, '\t', relative_frequencies[theme].get("political",0))

	
Geography 	 1.2693476366820498
Science 	 0.04007560125975222
Technology 	 0.15565601592546477
History 	 1.5371114730559727
Health, medicine and disease 	 0.1019053168198824
Everyday life 	 0.3722476284937062
Arts 	 0.5589647531228565
Philosophy and religion 	 0.854642455099992
Society and social sciences 	 2.694244853831445
Mathematics 	 0.007387064368648695
People 	 1.151769761475266
>>> L[-20:]
['hypothesis.measurement', 'iannis', 'psychophysicist', 'positive".type', 'foundation.ucla', 'caramuel', 'implemented.other', 'study.documenting', 'resampling', '2019-06-16', 'sampling.today', 'doi:10.1037/0003-066x.45.12.1304', 'population.sampling', 'overgeneralized', '1855693', 'false.referring', '1991).)the', 'semi-standardized', 'education).when', 'warne']
>>> L[:20]
['political', 'empire', 'her', 'war', 'food', 'government', 'south', 'plants', 'southern', 'men', 'low', 'germany', 'disease', 'blood', 'economy', 'sexual', 'party', 'london', 'ocean', 'film']
>>> L = sorted(thematic_article_word_counts["Mathematics"].keys(), key = lambda word: relative_frequencies["Mathematics"][word], reverse=True)
>>> L[:20]
['formulas.until', 'numbers(q).{\\displaystyle', 'integers(z){\\displaystyle', 'science.perhaps', 'equations;partial', 'mathematicians.the', 'arithmetic—will', 'space.nowadays', 'consideration.mathematics', 'mathematic(al', 'intuitively.the', 'deformationsalgebraic', 'shapesgraph', 'point-of-view', 'mathēmatikós', 'preempted', 'discovery".mathematical', 'geometry;homological', 'unexpectedness', 'areas.at']
>>> len(L)
21946
>>> L = [x for x in L if thematic_article_word_counts["Mathematics"][x] > 1]
>>> len(L)
7503
>>> L.sort(key = lambda word: relative_frequencies["Mathematics"][word], reverse=True)
>>> L[:30]
['algebralie', 'sautoy', 'hamel', 'girard', 'tékhnē', 'máthēma', 'homeomorphism', 'subfields.a', 'λ-calculus', 'pseudocode', 'programmingwhen', "rosser's", 'sogoto', 'if-then-else', "minsky's", "lambek's", 'quadruples', 'description"...prose', 'post–turing', 'ἀριθμός', 'divide-and-conquer', '3009', 'tabu', 'arithmos', 'thendone', 'contrivances', 'decrement', 'gotos', 'subproblem', 'barkley']
>>> L[:50]
['algebralie', 'sautoy', 'hamel', 'girard', 'tékhnē', 'máthēma', 'homeomorphism', 'subfields.a', 'λ-calculus', 'pseudocode', 'programmingwhen', "rosser's", 'sogoto', 'if-then-else', "minsky's", "lambek's", 'quadruples', 'description"...prose', 'post–turing', 'ἀριθμός', 'divide-and-conquer', '3009', 'tabu', 'arithmos', 'thendone', 'contrivances', 'decrement', 'gotos', 'subproblem', 'barkley', "knuth's", 'subproblems', 'knapsack', 'calculability', 'tausworthe', 'formalizations', "algorithm's", 'tallying', 'memoization', "kleene's", 'letter(s', 'proof-theorem', 'ifx2{\\displaystyle', '2}}}is', '2b2', '2}}^{\\sqrt', 'halmos', 'refutable', '□', 'contraposition']
>>> L[-30:]
['water', 'dna', 'air', 'kingdom', 'death', 'community', 'home', 'god', 'nuclear', 'against', 'islands', 'black', 'solar', 'united', 'country', 'production', 'religious', 'nations', 'africa', 'military', 'economic', 'city', 'animals', 'cultural', 'asia', 'national', 'countries', 'south', 'government', 'war']
>>> L = [x for x in L if thematic_article_word_counts["Mathematics"][x] > 5]
>>> len(L)
3037
>>> L.sort(key = lambda word: relative_frequencies["Mathematics"][word], reverse=True)
>>> L[:50]
['homeomorphism', 'subproblems', '2}}}is', 'bijection', 'p(n', 'nonnegative', 'countably', 'ofn{\\displaystyle', 'i\\in', 'y\\in', '−∞', 'preimage', 'reals', 'antiderivative', 'polytopes', 'hausdorff', 'arctan', 'oeis', 'gregory–leibniz', 'numbern{\\displaystyle', 'semiring', '−π', 'log10', 'bisector', 't={\\tfrac', "goldbach's", 'minuend', 'subtrahend', 'primality', 'zfc', 'codomain', 'surjection', 'b\\neq', '∈', 'surjective', '⊂', '∩', '∪', 'injective', 'p(s', 'f(a', 'x}such', 'y}is', '≠', 'x\\to', 'f\\circ', '1/x', 'multi-valued', 'f\\colon', 'real-valued']
>>> current_theme = "Art"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    current_theme = "Art"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
KeyError: 'Art'
>>> current_theme = "Arts"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
>>> L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
>>> L[:30]
['crosshatching', 'τεκτων', 'kiefer', 'andculinary', 'cinema.some', 'criticismtelevision', 'user.in', 'educationthe', 'artivism).modern', 'dance.other', 'venatoria', 'agricultura', 'tickets.within', 'theasthai', 'include:visual', 'draftswoman', 'coquinaria', 'criticismart', 'criticismliterary', 'criticismfilm', 'littera', 'non-artistic', 'mechanicae', 'criticismtheatre', 'art".the', 'tekton', 'undergo.as', 'one-person', 'neuvième', 'dictionariesdefinition']
>>> current_theme = "Science"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L[:30]
['know".there', 'double-check', 'skh1-io', 'inexpert', 'environments.science', 'relativism.finally', 'research.many', 'pursuance', 'sciencelist', 'secāre', 'speculation]".science', 'sciens', 'nescīre', 'science".modern', 'biased.some', 'sekh', 'sḱʰeh2(i', 'anti-scienceindex', "somerville's", 'self-criticism.aristotle', 'skije', 'lemaître.the', 'universe.science', 'causes.during', 'it.popper', 'skijo', 'austrian-british', 'results:scientific', 'non-aristotelian', 'over-simplified']
>>> current_theme = "Science"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = [x for x in L if thematic_article_word_counts["Mathematics"][x] >= 3]; L[:30]
['vec', 'hamiltonian', 'spacetime', 'atom', 'gravitational', 'thermodynamics', 'hydronium', 'entropy', 'ions', 'orbits', 'molecules', 'particle', 'lorentz', 'superposition', 'momentum', 'sn', 'hydrogen', 'brightness', 'tail', 'planets', 'cones', 'stars', 'spiral', 'tau', "object's", '±', 'ph', 'tails', 'relativity', 'si']
>>> current_theme = "People"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = [x for x in L if thematic_article_word_counts["Mathematics"][x] >= 3]; L[:30]
['noether', 'noetherian', 'gödel', 'disquisitiones', 'invariants', "turing's", 'erlangen', 'she', 'gordan', 'him', "al-khwarizmi's", 'turing', 'unpublished', 'königsberg', 'leonardo', 'my', "gödel's", 'archimedes', 'lectures', 'me', 'muḥammad', 'abraham', 'he', 'li', 'plato', 'einstein', 'cavalieri', 'his', 'father', 'al-dīn']
>>> current_theme = "People"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = [x for x in L if thematic_article_word_counts["Mathematics"][x] >= 3]; L[-30:]
['cryptography', 'perpendicular', 'noun', 'sector', 'hardware', 'holes', 'optimal', 'differentiation', 'billion', 'molecules', 'sports', 'networks', 'tfrac', 'simplest', 'dense', '3d', 'temperature', 'alphabet', 'processing', 'disk', 'processed', 'beta', 'outcomes', 'digits', 'reduces', 'software', 'depending', 'cells', 'frac', 'decrease']
>>> current_theme = "People"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = [x for x in L if thematic_article_word_counts["Mathematics"][x] >= 0]; L[-30:]
['cuisine', 'inca', 'asthma', 'cells', 'flows', 'viral', 'sustainable', 'kenya', 'enzymes', 'behaviors', '°f', 'globalization', 'mahāyāna', 'frac', 'algae', 'amazon', 'environments', 'nigeria', 'neutron', 'molecule', 'decrease', 'emissions', 'crust', 'electron', 'aluminium', 'dam', 'nutrients', 'genes', 'immune', 'insurance']
>>> current_theme = "People"; L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True); L = [x for x in L if thematic_article_word_counts["Mathematics"][x] >= 0]; L[:30]
['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
>>> for theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	print(theme, L[:30])

	
Geography ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Science ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Technology ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
History ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Health, medicine and disease ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Everyday life ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Arts ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Philosophy and religion ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Society and social sciences ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
Mathematics ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
People ['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]
>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	print(f"{theme}\n{L[:30]}\n")

	
People
['dictionarytopic', 'international)institute', 'dreses', 'oceans.karl', '1934–2016', 'equi-azimuthal', 'subject.over', 'flow.carl', 'populations.regional', 'projection.abu', 'represent.the', 'rgs', 'al-kashgari', 'guyot', 'geographicprofessional', 'mapsjournal', 'geographers.eratosthenes', 'geography.walter', 'sciencejournal', '1863–1932', 'meridians.the', "founder's", '6,356.7', "information's", "geography's", 'geographia.radhanath', 'erosion.yi-fu', 'distant"tobler\'s', 'pakistan)national', 'archaeologist.mark']

People
['know".there', 'double-check', 'skh1-io', 'inexpert', 'environments.science', 'relativism.finally', 'research.many', 'pursuance', 'sciencelist', 'secāre', 'speculation]".science', 'sciens', 'nescīre', 'science".modern', 'biased.some', 'sekh', 'sḱʰeh2(i', 'anti-scienceindex', "somerville's", 'self-criticism.aristotle', 'skije', 'lemaître.the', 'universe.science', 'causes.during', 'it.popper', 'skijo', 'austrian-british', 'results:scientific', 'non-aristotelian', 'over-simplified']

People
['role.continuing', 'unemployment.between', 'techno-material', 'borgmann', 'τεχνολογία', '90-120', 'life.prominent', 'fire-use', 'paved.ancient', 'singularity.major', 'society.some', 'singularitarianism.the', 'cyberethics', 'technopaganism', 'nanobots', 'travois', 'ecovillage', 'unabomber', 'technologie', 'culture."initially', 'technology.various', 'intelligence.in', 'gattaca', 'anti-technology', 'health.recent', 'uploading', 'efforts.despite', 'be."the', 'techno-utopianism', 'techno-utopian']

People
['vi.1383', '5723', 'trevelyan', 'history.herodotus', 'before.archeology', 'stær', 'period.marxist', 'history/geography', 'groups.environmental', 'childhoodhistory', 'superpatriotism', 'iraq).history', 'inrdp', 'rowbotham', 'tenure-track', 'unsoughtby', 'recurring.there', 'ἵστωρ', "windschuttle's", 'mousnier', "historywomen's", 'excavator', 'economy.at', 'koonz', 'hans-ulrich', 'found.history', 'generations.this', 'meta-level', 'europe.history', 'hemisphere.history']

People
['widespread.lepers', 'changes.some', 'example.morbiditymorbidity', 'airbornean', 'diseaseone', 'prediabetes', 'predisposes', 'diseases.pathosis', 'cured.clinical', 'phase.recoveryrecovery', 'pre-cancer', 'sequela', 'nosology', "disease's", 'health-risk', 'louis"man', 'cancerbenefit', 'qaly', 'diseasea', 'noted.terminal', 'pain.treatment', 'outcome.idiopathic', 'aggression.some', 'subclinical/prodromal/premonitory', 'organ.a', 'predisease', 'stigma.social', 'air.foodbornefoodborne', 'syndemic', 'famine-prone']

People
['scratchy', 'items.clothing', "fabric's", '2010hollander', 'last-common-ancestor', 'bootcut', 'garment.another', 'zippers', 'raveled', 'tracksuits', 'semi-formal', 'daywear', 'cadarett', "imperialist's", 'wet."tactile', 'shabby.clothing', '0-08-044466-0', 'hanboks', 'look.in', 'kilts', 'stoneking—anthropologists', 'togas', 'biodegradable.excess', 'sensations.pressure', '0-8031-3488-6', 'palaoa', 'costume.clothing', 'purposes.many', 'doi:10.2165/00007256-200333130-00001', 'ago.kittler']

People
['crosshatching', 'τεκτων', 'kiefer', 'andculinary', 'cinema.some', 'criticismtelevision', 'user.in', 'educationthe', 'artivism).modern', 'dance.other', 'venatoria', 'agricultura', 'tickets.within', 'theasthai', 'include:visual', 'draftswoman', 'coquinaria', 'criticismart', 'criticismliterary', 'criticismfilm', 'littera', 'non-artistic', 'mechanicae', 'criticismtheatre', 'art".the', 'tekton', 'undergo.as', 'one-person', 'neuvième', 'dictionariesdefinition']

People
['indeterminism', 'incompatibilist', 'religiō', 'rebirths', 'ḥadīth', 'narrow.some', 'śūnyatā', 'mimāmsā', 'mazdakism', 'pudgalavāda', 'division.this', 'philosophersphilosophy', 'trebek', 'economics.today', 'σοφία', 'êthika', 'well-lived', 'elements.during', 'adharma', 'uncreated.some', "physics')in", 'eras:ancient', 'camac', 'philosopher-scholars', 'vijñapti-matra', 'cyrenaicism', 'akkadian.early', '1000–500', 'history.islamic', 'theosophy.the']

People
['culturesemiotics', 'movements—such', 'inhibit—social', 'hymes', '528–29.middleton', 'giroux.wilson', 'swatos', 'press.tylor', 'subjects.other', 'kulturbrille', 'hoggart', 'holquist', 'society.cultures', 'reconception', 'feminism.petrakis', 'global-local', '978-0-19-288051-2findley', '978-0-252-06445-6.barzilai', '1767–1835', '2006-07-10.reagan', 'uncorrupted', '1921–1988', 'dispositions.when', '9780393038385.ralph', 'rothney', 'group.accepting', '2014-12-27', "978-0-335-15275-9.o'neil", 'group.cultural', 'gilroy.in']

People
['formulas.until', 'numbers(q).{\\displaystyle', 'integers(z){\\displaystyle', 'science.perhaps', 'equations;partial', 'mathematicians.the', 'arithmetic—will', 'space.nowadays', 'consideration.mathematics', 'mathematic(al', 'intuitively.the', 'deformationsalgebraic', 'shapesgraph', 'point-of-view', 'mathēmatikós', 'preempted', 'discovery".mathematical', 'geometry;homological', 'unexpectedness', 'areas.at', 'rigor".the', 'algebralie', 'philosophically-minded', 'dimensions.in', 'geometryconvex', 'opinion—sometimes', 'theory;commutative', 'length.differential', 'polynomialstopology', 'al-ṭūsī.during']

People
['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]

>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	print(f"{current_theme}\n{L[:30]}\n")

	
Geography
['dictionarytopic', 'international)institute', 'dreses', 'oceans.karl', '1934–2016', 'equi-azimuthal', 'subject.over', 'flow.carl', 'populations.regional', 'projection.abu', 'represent.the', 'rgs', 'al-kashgari', 'guyot', 'geographicprofessional', 'mapsjournal', 'geographers.eratosthenes', 'geography.walter', 'sciencejournal', '1863–1932', 'meridians.the', "founder's", '6,356.7', "information's", "geography's", 'geographia.radhanath', 'erosion.yi-fu', 'distant"tobler\'s', 'pakistan)national', 'archaeologist.mark']

Science
['know".there', 'double-check', 'skh1-io', 'inexpert', 'environments.science', 'relativism.finally', 'research.many', 'pursuance', 'sciencelist', 'secāre', 'speculation]".science', 'sciens', 'nescīre', 'science".modern', 'biased.some', 'sekh', 'sḱʰeh2(i', 'anti-scienceindex', "somerville's", 'self-criticism.aristotle', 'skije', 'lemaître.the', 'universe.science', 'causes.during', 'it.popper', 'skijo', 'austrian-british', 'results:scientific', 'non-aristotelian', 'over-simplified']

Technology
['role.continuing', 'unemployment.between', 'techno-material', 'borgmann', 'τεχνολογία', '90-120', 'life.prominent', 'fire-use', 'paved.ancient', 'singularity.major', 'society.some', 'singularitarianism.the', 'cyberethics', 'technopaganism', 'nanobots', 'travois', 'ecovillage', 'unabomber', 'technologie', 'culture."initially', 'technology.various', 'intelligence.in', 'gattaca', 'anti-technology', 'health.recent', 'uploading', 'efforts.despite', 'be."the', 'techno-utopianism', 'techno-utopian']

History
['vi.1383', '5723', 'trevelyan', 'history.herodotus', 'before.archeology', 'stær', 'period.marxist', 'history/geography', 'groups.environmental', 'childhoodhistory', 'superpatriotism', 'iraq).history', 'inrdp', 'rowbotham', 'tenure-track', 'unsoughtby', 'recurring.there', 'ἵστωρ', "windschuttle's", 'mousnier', "historywomen's", 'excavator', 'economy.at', 'koonz', 'hans-ulrich', 'found.history', 'generations.this', 'meta-level', 'europe.history', 'hemisphere.history']

Health, medicine and disease
['widespread.lepers', 'changes.some', 'example.morbiditymorbidity', 'airbornean', 'diseaseone', 'prediabetes', 'predisposes', 'diseases.pathosis', 'cured.clinical', 'phase.recoveryrecovery', 'pre-cancer', 'sequela', 'nosology', "disease's", 'health-risk', 'louis"man', 'cancerbenefit', 'qaly', 'diseasea', 'noted.terminal', 'pain.treatment', 'outcome.idiopathic', 'aggression.some', 'subclinical/prodromal/premonitory', 'organ.a', 'predisease', 'stigma.social', 'air.foodbornefoodborne', 'syndemic', 'famine-prone']

Everyday life
['scratchy', 'items.clothing', "fabric's", '2010hollander', 'last-common-ancestor', 'bootcut', 'garment.another', 'zippers', 'raveled', 'tracksuits', 'semi-formal', 'daywear', 'cadarett', "imperialist's", 'wet."tactile', 'shabby.clothing', '0-08-044466-0', 'hanboks', 'look.in', 'kilts', 'stoneking—anthropologists', 'togas', 'biodegradable.excess', 'sensations.pressure', '0-8031-3488-6', 'palaoa', 'costume.clothing', 'purposes.many', 'doi:10.2165/00007256-200333130-00001', 'ago.kittler']

Arts
['crosshatching', 'τεκτων', 'kiefer', 'andculinary', 'cinema.some', 'criticismtelevision', 'user.in', 'educationthe', 'artivism).modern', 'dance.other', 'venatoria', 'agricultura', 'tickets.within', 'theasthai', 'include:visual', 'draftswoman', 'coquinaria', 'criticismart', 'criticismliterary', 'criticismfilm', 'littera', 'non-artistic', 'mechanicae', 'criticismtheatre', 'art".the', 'tekton', 'undergo.as', 'one-person', 'neuvième', 'dictionariesdefinition']

Philosophy and religion
['indeterminism', 'incompatibilist', 'religiō', 'rebirths', 'ḥadīth', 'narrow.some', 'śūnyatā', 'mimāmsā', 'mazdakism', 'pudgalavāda', 'division.this', 'philosophersphilosophy', 'trebek', 'economics.today', 'σοφία', 'êthika', 'well-lived', 'elements.during', 'adharma', 'uncreated.some', "physics')in", 'eras:ancient', 'camac', 'philosopher-scholars', 'vijñapti-matra', 'cyrenaicism', 'akkadian.early', '1000–500', 'history.islamic', 'theosophy.the']

Society and social sciences
['culturesemiotics', 'movements—such', 'inhibit—social', 'hymes', '528–29.middleton', 'giroux.wilson', 'swatos', 'press.tylor', 'subjects.other', 'kulturbrille', 'hoggart', 'holquist', 'society.cultures', 'reconception', 'feminism.petrakis', 'global-local', '978-0-19-288051-2findley', '978-0-252-06445-6.barzilai', '1767–1835', '2006-07-10.reagan', 'uncorrupted', '1921–1988', 'dispositions.when', '9780393038385.ralph', 'rothney', 'group.accepting', '2014-12-27', "978-0-335-15275-9.o'neil", 'group.cultural', 'gilroy.in']

Mathematics
['formulas.until', 'numbers(q).{\\displaystyle', 'integers(z){\\displaystyle', 'science.perhaps', 'equations;partial', 'mathematicians.the', 'arithmetic—will', 'space.nowadays', 'consideration.mathematics', 'mathematic(al', 'intuitively.the', 'deformationsalgebraic', 'shapesgraph', 'point-of-view', 'mathēmatikós', 'preempted', 'discovery".mathematical', 'geometry;homological', 'unexpectedness', 'areas.at', 'rigor".the', 'algebralie', 'philosophically-minded', 'dimensions.in', 'geometryconvex', 'opinion—sometimes', 'theory;commutative', 'length.differential', 'polynomialstopology', 'al-ṭūsī.during']

People
['diyarbekir', 'extols', 'conflict.hammurabi', 'marduk:after', 'delitzsch', 'straddled', 'tukrish', 'duplicity', 'amorites".vast', 'irredeemably', 'gutium', 'puzur-sin', 'adasi', 'punishment.a', 'sippar.thus', 'founding.the', 'weinman', 'retribution.the', 'compels', 'täuschung', 'sealand', 'amraphel', 'hammurabi-ili', 'bibel', '14:1', 'talionis', 'hammurabi.in', 'similarities.hammurabi', 'bel-ibni', "amraphael's"]

>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 3]
	print(f"{current_theme}\n{L[:30]}\n")

	
Geography
['geoscheme', 'physiographically', 'subcontinents', 'continentlist', 'trended', 'berber-speaking', 'coltan', 'oau', 'sealers', "d'urville", 'bransfield', "d'étatthe", 'ἀσία', 'emba', 'malala', 'carpathians', 'volga–don', '55th', 'laramide', 'monterrey', 'physiographic', 'megaregions', 'cup.the', 'cisplatina', 'pre-ceramic', 'solimões', 'argentines', 'neuquén', 'bouvet', 'aconcagua']

Science
['hypothetico-deductive', "hole's", 'backbones', 'fleck', 'smm7', 'sievert', 'kcd', 'millionth', '80000', '10−24', 'μg', 'thermometry', 'dyne', 'bipm', 'jansky', '10−6', 'radiometry', 'deformational', 'extrasolar', 'calcified', 'nucleosynthesis', '1006', 'gravitational-wave', 'reionization', 'astrometry', 'stars.the', 'oort', 'interferometer', 'eject', 'protostar']

Technology
['television.the', 'cnc', "engineer's", 'pmma', 'hvac', 'fea', 'flashlights', 'a·h', 'mwh', 'nameplate', 'overcharging', 'deflagrate', 'hmx', 'detonators', 'detonator', 'semi-smokeless', 'ici', 'flintlocks', 'al-rammah', 'igcc', 'bituminous', 'precombustion', 'butane', 'mj/m3', 'pentane', 'hvhf', 'kwh/lb', 'decatherms', 'thermal-neutron', 'baseload']

History
['trevelyan', 'excavator', 'hemisphere.history', 'furet', 'historyhistory', 'kenyanthropus', 'pratihara', 'voyaging', 'mutapa', 'akwamu', 'landholding', 'ethno-cultural', 'hephthalites', 'butua', 'thalassocracy', 'tawantinsuyu', 'taebong', '1340s', 'puebloans', 'geledi', 'peiligang', 'pengtoushan', 'turchin', 'isao', 'korotayev', 'kardashev', 'mesoamerica.the', 'rudeness', 'hoes', 'lomekwi']

Health, medicine and disease
['prediabetes', 'sequela', 'qaly', 'diseasea', 'predisease', 'neuropsychiatric', 'medlineplus', 'allergists', 'atopy', 'conjunctivitis', 'bronchoconstriction', 'internist', 'urushiol', 'intubation', 'chloroquine', 'spacer', 'asthma-related', 'sinusitis', 'metastasize', 'colitis', 'uspstf', 'hypermethylated', 'strep', 'myocarditis', 'clopidogrel', 'nasogastric', 'hypoperfusion', 'epidural', 'thrombectomy', 'hematomas']

Everyday life
['brides', 'stepfamilies', 'mahr', 'somerford', 'uninvolved', 'foreplay', 'nsshb', 'erotically', 'asexuality', 'soce', 'ulrichs', 'saso', 'gender-role', 'masculinities', 'wer', 'hcas', 'blanching', 'maillard', 'braising', 'cookery', 'cereus', 'steeping', 'pumpkin', 'sweeteners', 'saltiness', 'tartare', 'lactobacilli', 'caryopsis', 'spikelets', 'anti-nutritional']

Arts
['littera', 'photojournalism', 'symbolistic', 'nibelungen', "goya's", 'lo-fi', 'urinal', 'zegher', 'non-motivated', 'bronzework', "hirst's", 'beuys', "emin's", 'tanagra', 'intentionalism', 'stoneware', 'kotosh', 'ready-to-wear', 'anti-fashion', 'roxy', 'marciano', 'hard-edge', "gorky's", 'kupka', 'františek', 'well-made', 'stoppard', 'rimbaud', 'intermedia', 'twelve-tone']

Philosophy and religion
['indeterminism', 'incompatibilist', 'religiō', 'rebirths', 'ḥadīth', 'śūnyatā', '1000–500', 'darśana', 'sub-schools', 'epoché', 'sarvāstivāda', 'pramāṇa', 'geonim', 'hedonist', 'coherentists', 'shunyata', 'metaepistemology', 'dignaga', "quine's", 'uninformative', 'carvaka', 'anumāṇa', 'knowledge-that', 'belief-that', 'interpretationism', 'thatp{\\displaystyle', 'nonbelievers', 'inclusivism', 'subject-centred', 'eikasia']

Society and social sciences
['hoggart', 'childlore', 'mushaf', 'counter-power', 'decision-maker', 'facilitative', 'extroverts', 'slobodan', 'lexemes', 'bowlby', 'maslow', 'verstehen', 'vilfredo', 'antipositivism', '2015."home', 'non-capitalist', 'anti-racism', 'lazarsfeld', 'trelawny', 'left–right', 'mother-countries', 'bastiat', 'sortition', 'trotskyists', 'rojava', 'seizes', 'recallable', 'engelbert', 'salvadoran', 'ferrer']

Mathematics
['homeomorphism', 'pseudocode', "minsky's", 'subproblems', 'calculability', 'tallying', 'memoization', '2}}}is', '2}}^{\\sqrt', 'halmos', 'contraposition', 'bijection', 'p(n', 'thenx{\\displaystyle', 'nonnegative', 'set-builder', 'countably', 'ofn{\\displaystyle', 'nonempty', 'preimagef−1(y){\\displaystyle', 'nonpositive', 'r,\\theta', 'i\\in', 'y\\in', '−∞', 'setc{\\displaystyle', 'preimage', 'g\\colon', 'f.if', 'reals']

People
['delitzsch', 'ramose', 'sobekneferu', 'el-bahri', 'djeser-djeseru', 'co-regent', 'hers', 'maatkare', "ramesses's", 'ramesseum', 'el-wali', 'n.s', 'defecting', 'cassandane', 'kuraš', 'ambhi', 'arrhidaeus', 'roused', 'cleitus', 'thessalus', 'thrasyllus', 'swarthy', 'massaga', 'aspasioi', 'veratrum', 'apelles', "porus's", 'bourrienne', 'jambudvipa', 'vitashoka']

>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: total_word_count[word] * relative_frequencies[current_theme][word], reverse=True)
	L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 3]
	print(f"{current_theme}\n{L[:30]}\n")

	
Geography
['the', 'of', 'and', 'in', 'to', 'a', 'is', 'as', 'by', 'with', 'was', 'are', 'for', 'from', 'on', 'has', 'that', 'which', 'it', 'its', 'at', 'were', 'an', 'or', 'have', 'also', 'world', 'city', 'most', 'been']

Science
['the', 'of', 'and', 'in', 'a', 'to', 'is', 'as', 'are', 'that', 'by', 'for', 'with', 'or', 'from', 'be', 'which', 'on', 'it', 'an', 'have', 'this', 'can', 'at', 'such', 'was', 'other', 'their', 'not', 'has']

Technology
['the', 'of', 'and', 'to', 'a', 'in', 'is', 'as', 'for', 'or', 'by', 'are', 'that', 'with', 'be', 'on', 'from', 'was', 'used', 'an', 'it', 'which', 'can', 'such', 'at', 'this', 'have', 'use', 'also', 'were']

History
['the', 'of', 'and', 'in', 'to', 'a', 'was', 'as', 'by', 'were', 'with', 'from', 'for', 'that', 'on', 'which', 'is', 'it', 'at', 'an', 'had', 'their', 'this', 'empire', 'or', 'century', 'his', 'war', 'also', 'its']

Health, medicine and disease
['the', 'of', 'and', 'in', 'to', 'a', 'is', 'as', 'for', 'or', 'are', 'with', 'that', 'by', 'be', 'from', 'may', 'an', 'have', 'on', 'can', 'it', 'health', 'was', 'disease', 'not', 'which', 'also', 'such', 'this']

Everyday life
['the', 'of', 'and', 'in', 'to', 'a', 'is', 'as', 'for', 'or', 'are', 'that', 'with', 'by', 'from', 'be', 'on', 'have', 'it', 'such', 'which', 'was', 'an', 'their', 'this', 'also', 'games', 'not', 'at', 'other']

Arts
['the', 'of', 'and', 'in', 'a', 'to', 'as', 'is', 'by', 'with', 'or', 'that', 'for', 'was', 'from', 'music', 'are', 'on', 'which', 'an', 'were', 'be', 'it', 'such', 'art', 'this', 'have', 'also', 'century', 'at']

Traceback (most recent call last):
  File "<pyshell#423>", line 5, in <module>
    print(f"{current_theme}\n{L[:30]}\n")
KeyboardInterrupt
>>> import math
>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
	L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 3]
	print(f"{current_theme}\n{L[:30]}\n")

	
Geography
['lagos', 'lake', 'airport', 'jakarta', 'paulo', 'lakes', 'são', 'city', "city's", 'reef', 'saudi', 'sq', 'uae', 'mumbai', 'gdp', "country's", 'metro', 'km2', 'country', 'largest', 'ranked', 'myanmar', 'mississippi', 'river', 'amazon', 'tokyo', 'metropolitan', 'nigeria', 'bangladesh', 'mi']

Science
['atoms', 'electrons', 'molecules', 'cells', 'particles', 'electron', 'hydrogen', 'galaxies', 'organisms', 'rna', 'particle', 'dna', 'stars', 'neutron', 'oxygen', 'gravitational', 'protons', 'planet', 'aluminium', 'neutrons', 'archaea', 'milky', 'nuclei', 'planets', 'clouds', 'atom', "earth's", 'molecular', 'quarks', 'species']

Technology
['engines', 'engine', 'knife', 'motors', 'concrete', 'radar', 'robots', 'rotor', 'turbine', 'exhaust', 'rocket', 'fuel', 'combustion', 'battery', 'lasers', 'refrigeration', 'laser', 'explosives', 'batteries', 'aircraft', 'turbines', 'clocks', 'piston', 'robot', 'dam', 'propellant', 'firearm', 'transistors', 'phones', 'cryptography']

History
['maya', 'empire', 'crusade', 'inca', 'tang', 'aztec', 'harappan', 'viking', 'crusades', 'mesoamerican', 'byzantine', 'artaxerxes', 'silk', 'mesoamerica', 'vikings', 'postclassic', 'plague', 'han', 'gupta', 'dynasty', 'ottoman', 'archaeology', 'crusaders', 'alexios', 'mongol', 'preclassic', 'civilization', 'crusader', 'xiongnu', 'empires']

Health, medicine and disease
['asthma', 'influenza', 'diabetes', 'pneumonia', 'infection', 'vaccine', 'malaria', 'nurses', 'tb', 'anesthesia', 'symptoms', 'addiction', 'vaccines', 'obesity', 'stroke', 'hiv', 'smallpox', 'nursing', 'antibiotics', 'variola', 'disease', 'medications', 'cancer', 'ageing', 'diagnosis', 'anesthetic', 'hygiene', 'tuberculosis', 'smoking', 'hemorrhagic']

Everyday life
['games', 'milk', 'jewellery', 'tea', 'athletics', 'coffee', 'toys', 'adolescents', 'soybean', 'ioc', 'soy', 'cheese', 'intercourse', 'game', 'soybeans', 'adolescence', 'potato', 'maize', 'cheeses', 'sexual', 'athletes', 'parenting', 'olympic', 'heterosexual', 'adolescent', 'wheat', 'gambling', 'potatoes', 'flour', 'rice']

Arts
['jazz', 'fairy', 'pianos', 'comics', 'music', 'orchestras', 'piano', 'tales', 'opera', 'animation', 'blues', 'romanticism', 'musical', 'orchestra', 'modernism', 'strings', 'bass', '•', 'sculpture', 'dance', 'vocal', 'instruments', 'khufu', 'musicians', 'pyramid', 'improvisation', 'singers', 'punk', 'bebop', 'operas']

Philosophy and religion
['mahāyāna', 'talmud', 'gita', 'meditation', 'kami', 'guru', 'theravāda', 'shinto', 'prayer', 'shīʿa', 'sikh', 'determinism', 'bhagavad', 'yoga', 'truth', 'jain', 'krishna', 'ahl', 'ontology', 'torah', 'ʿalī', 'sikhs', 'atheism', 'karma', 'granth', 'god', 'dharma', 'epistemology', 'quran', 'hinduism']

Society and social sciences
['insurance', 'vowel', 'dialects', 'privacy', 'vowels', 'alphabet', 'consonant', 'verbs', 'cyrillic', 'consonants', 'socialism', 'abortion', 'anger', 'anarchism', 'sociology', 'nouns', 'globalization', 'feminism', 'capitalism', 'verb', 'language', 'conservatism', 'grammatical', 'icrc', 'script', 'discrimination', 'anarchists', 'racism', 'linguistics', 'grammar']

Mathematics
['mathbb', 'integers', 'π', 'algebraic', 'triangle', 'logarithm', 'nth', 'integer', 'tfrac', 'algebra', 'x', 'denominator', 'conic', 'geometry', 'polygon', 'exponentiation', 'euclidean', 'fractions', 'multiplication', 'primes', 'digits', 'infinity', 'combinatorics', 'numbers', 'algorithm', 'polynomial', 'sqrt', '0', 'topological', 'topology']

People
['his', 'he', 'him', 'her', 'she', 'mandela', 'chaplin', 'gandhi', 'tesla', 'edison', 'lincoln', 'jackson', 'bolívar', 'nietzsche', 'ashoka', 'rembrandt', 'beatles', 'jesus', 'akbar', 'bach', 'wollstonecraft', 'ford', 'freud', 'noether', 'tolstoy', 'kahlo', 'mao', 'socrates', 'moses', "jackson's"]

>>> with open("themed_vectors.txt", 'w') as file:
	for current_theme in relative_frequencies:
		file.write(theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for word in L:
			file.write(word + '\t' + str(relative_frequencies[current_theme]))

			
8
Traceback (most recent call last):
  File "<pyshell#433>", line 9, in <module>
    file.write(word + '\t' + str(relative_frequencies[current_theme]))
  File "C:\Users\Alastair\AppData\Local\Programs\Python\Python39\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode characters in position 7765-7767: character maps to <undefined>
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		file.write(theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for word in L:
			file.write(word + '\t' + str(relative_frequencies[current_theme]))

			
8
2375440
2375448
2375431
2375436
2375434
Traceback (most recent call last):
  File "<pyshell#435>", line 9, in <module>
    file.write(word + '\t' + str(relative_frequencies[current_theme]))
KeyboardInterrupt
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		dummy = file.write(theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for word in L:
			file.write(word + '\t' + str(relative_frequencies[current_theme]))

			
2375440
2375448
2375431
2375436
2375434
2375439
2375437Traceback (most recent call last):
  File "<pyshell#437>", line 9, in <module>
    file.write(word + '\t' + str(relative_frequencies[current_theme]))
KeyboardInterrupt
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for word in L:
			file.write(word + '\t' + str(relative_frequencies[current_theme]))

			
Geography
2375440
2375448
2375431
2375436
2375434
2375439
2375437
Traceback (most recent call last):
  File "<pyshell#439>", line 10, in <module>
    file.write(word + '\t' + str(relative_frequencies[current_theme]))
KeyboardInterrupt
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:100]
		for word in L:
			dummy = file.write(word + '\t' + str(relative_frequencies[current_theme]))

			
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> f = open("themed_vectors.txt")
>>> L = [lines for line in f]
Traceback (most recent call last):
  File "<pyshell#443>", line 1, in <module>
    L = [lines for line in f]
  File "<pyshell#443>", line 1, in <listcomp>
    L = [lines for line in f]
NameError: name 'lines' is not defined
>>> L = [line for line in f]
Traceback (most recent call last):
  File "<pyshell#444>", line 1, in <module>
    L = [line for line in f]
  File "<pyshell#444>", line 1, in <listcomp>
    L = [line for line in f]
  File "C:\Users\Alastair\AppData\Local\Programs\Python\Python39\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 2356: character maps to <undefined>
>>> f.close()
>>> f = open("themed_vectors.txt", encoding="utf-8")
>>> L = [lines for line in f]
Traceback (most recent call last):
  File "<pyshell#447>", line 1, in <module>
    L = [lines for line in f]
  File "<pyshell#447>", line 1, in <listcomp>
    L = [lines for line in f]
NameError: name 'lines' is not defined
>>> L = [line for line in f]
Traceback (most recent call last):
  File "<pyshell#448>", line 1, in <module>
    L = [line for line in f]
  File "<pyshell#448>", line 1, in <listcomp>
    L = [line for line in f]
  File "C:\Users\Alastair\AppData\Local\Programs\Python\Python39\lib\codecs.py", line 319, in decode
    def decode(self, input, final=False):
KeyboardInterrupt
>>> f.close()
>>> f = open("themed_vectors.txt", encoding="utf-8")
>>> f.readline()
'GEOGRAPHY\n'
>>> f.readline()
'\n'
>>> f.readline()
Traceback (most recent call last):
  File "<pyshell#453>", line 1, in <module>
    f.readline()
  File "C:\Users\Alastair\AppData\Local\Programs\Python\Python39\lib\codecs.py", line 319, in decode
    def decode(self, input, final=False):
KeyboardInterrupt
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:3]
		for word in L:
			dummy = file.write(word + '\t' + str(relative_frequencies[current_theme])+'\n')

			
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:3]
		for word in L:
			dummy = file.write(word + '\t' + str(relative_frequencies[current_theme][word])+'\n')

			
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:3]
		for word in L:
			dummy = file.write(word + '\t' + str(relative_frequencies[current_theme][word])+'\n')
		print('\n')

		
Geography


Science


Technology


History


Health, medicine and disease


Everyday life


Arts


Philosophy and religion


Society and social sciences


Mathematics


People


>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:3]
		for word in L:
			dummy = file.write(word + '\t' + str(relative_frequencies[current_theme][word])+'\n')
		dummy = file.write('\n')

		
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:3]
		for i, word in enumerate(L):
			dummy = file.write(str(i) + '\t' + word + '\t' + str(relative_frequencies[current_theme][word])+'\n')
		dummy = file.write('\n')

		
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for i, word in enumerate(L):
			dummy = file.write(str(i) + '\t' + word + '\t' + str(relative_frequencies[current_theme][word])+'\n')
		dummy = file.write('\n')

		
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> file.close()
>>> f.close()
>>> with open("themed_vectors.csv", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for i, word in enumerate(L):
			dummy = file.write(str(i) + '\t' + word + '\t' + str(relative_frequencies[current_theme][word])+'\n')
		dummy = file.write('\n')

		
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> E = [word for word in total_word_count if ',' in word]
>>> len(E)
6515
>>> E[0]
'6,356.7'
>>> del E
>>> with open("themed_vectors.txt", 'w', encoding="utf-8") as file:
	for current_theme in relative_frequencies:
		print(current_theme)
		dummy = file.write(current_theme.upper()+'\n\n')
		L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
		#L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
		L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
		L = L[:5000]
		for i, word in enumerate(L):
			dummy = file.write(str(i) + '\t' + word + '\t' + str(relative_frequencies[current_theme][word])+'\n')
		dummy = file.write('\n')

		
Geography
Science
Technology
History
Health, medicine and disease
Everyday life
Arts
Philosophy and religion
Society and social sciences
Mathematics
People
>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
	L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 3]
	print(f"{current_theme}\n{', '.join(L[:20)]}\n")
	
SyntaxError: f-string: closing parenthesis ')' does not match opening parenthesis '['
>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
	L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 3]
	print(f"{current_theme}\n{', '.join(L[:20])}\n")

	
Geography
lagos, lake, airport, jakarta, paulo, lakes, são, city, city's, reef, saudi, sq, uae, mumbai, gdp, country's, metro, km2, country, largest

Science
atoms, electrons, molecules, cells, particles, electron, hydrogen, galaxies, organisms, rna, particle, dna, stars, neutron, oxygen, gravitational, protons, planet, aluminium, neutrons

Technology
engines, engine, knife, motors, concrete, radar, robots, rotor, turbine, exhaust, rocket, fuel, combustion, battery, lasers, refrigeration, laser, explosives, batteries, aircraft

History
maya, empire, crusade, inca, tang, aztec, harappan, viking, crusades, mesoamerican, byzantine, artaxerxes, silk, mesoamerica, vikings, postclassic, plague, han, gupta, dynasty

Health, medicine and disease
asthma, influenza, diabetes, pneumonia, infection, vaccine, malaria, nurses, tb, anesthesia, symptoms, addiction, vaccines, obesity, stroke, hiv, smallpox, nursing, antibiotics, variola

Everyday life
games, milk, jewellery, tea, athletics, coffee, toys, adolescents, soybean, ioc, soy, cheese, intercourse, game, soybeans, adolescence, potato, maize, cheeses, sexual

Arts
jazz, fairy, pianos, comics, music, orchestras, piano, tales, opera, animation, blues, romanticism, musical, orchestra, modernism, strings, bass, •, sculpture, dance

Philosophy and religion
mahāyāna, talmud, gita, meditation, kami, guru, theravāda, shinto, prayer, shīʿa, sikh, determinism, bhagavad, yoga, truth, jain, krishna, ahl, ontology, torah

Society and social sciences
insurance, vowel, dialects, privacy, vowels, alphabet, consonant, verbs, cyrillic, consonants, socialism, abortion, anger, anarchism, sociology, nouns, globalization, feminism, capitalism, verb

Mathematics
mathbb, integers, π, algebraic, triangle, logarithm, nth, integer, tfrac, algebra, x, denominator, conic, geometry, polygon, exponentiation, euclidean, fractions, multiplication, primes

People
his, he, him, her, she, mandela, chaplin, gandhi, tesla, edison, lincoln, jackson, bolívar, nietzsche, ashoka, rembrandt, beatles, jesus, akbar, bach

>>> for current_theme in relative_frequencies:
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: relative_frequencies[current_theme][word], reverse=True)
	L = sorted(thematic_article_word_counts[current_theme].keys(), key = lambda word: math.log(total_word_count[word]) * relative_frequencies[current_theme][word], reverse=True)
	L = [x for x in L if thematic_article_word_counts[current_theme][x] >= 0]
	print(f"{current_theme}\n{', '.join(L[:20])}\n")

	
Geography
lagos, lake, airport, jakarta, paulo, lakes, são, city, city's, reef, saudi, sq, uae, mumbai, gdp, country's, metro, km2, country, largest

Science
atoms, electrons, molecules, cells, particles, electron, hydrogen, galaxies, organisms, rna, particle, dna, stars, neutron, oxygen, gravitational, protons, planet, aluminium, neutrons

Technology
engines, engine, knife, motors, concrete, radar, robots, rotor, turbine, exhaust, rocket, fuel, combustion, battery, lasers, refrigeration, laser, explosives, batteries, aircraft

History
maya, empire, crusade, inca, tang, aztec, harappan, viking, crusades, mesoamerican, byzantine, artaxerxes, silk, mesoamerica, vikings, postclassic, plague, han, gupta, dynasty

Health, medicine and disease
asthma, influenza, diabetes, pneumonia, infection, vaccine, malaria, nurses, tb, anesthesia, symptoms, addiction, vaccines, obesity, stroke, hiv, smallpox, nursing, antibiotics, variola

Everyday life
games, milk, jewellery, tea, athletics, coffee, toys, adolescents, soybean, ioc, soy, cheese, intercourse, game, soybeans, adolescence, potato, maize, cheeses, sexual

Arts
jazz, fairy, pianos, comics, music, orchestras, piano, tales, opera, animation, blues, romanticism, musical, orchestra, modernism, strings, bass, •, sculpture, dance

Philosophy and religion
mahāyāna, talmud, gita, meditation, kami, guru, theravāda, shinto, prayer, shīʿa, sikh, determinism, bhagavad, yoga, truth, jain, krishna, ahl, ontology, torah

Society and social sciences
insurance, vowel, dialects, privacy, vowels, alphabet, consonant, verbs, cyrillic, consonants, socialism, abortion, anger, anarchism, sociology, nouns, globalization, feminism, capitalism, verb

Mathematics
mathbb, integers, π, algebraic, triangle, logarithm, nth, integer, tfrac, algebra, x, denominator, conic, geometry, polygon, exponentiation, euclidean, fractions, multiplication, primes

People
his, he, him, her, she, mandela, chaplin, gandhi, tesla, edison, lincoln, jackson, bolívar, nietzsche, ashoka, rembrandt, beatles, jesus, akbar, bach

>>> 
