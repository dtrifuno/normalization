from .base import Pipeline, Replacer
from .cardinals import cardinals2words
from .date import dates2words
from .ordinals import ordinal2words

REPLACEMENT_PATTERNS = {
    "civilis": "цивилис",
    "civis": "цивис",
    "civitas": "цивитас",
    "cella": "цела",
    "geospiza fortis": "геоспиза фортис",
    "geospiza conirostris": "геоспиза конирострис",
    "six days in fallujah": "сикс дејс ин фалуџа",
    "hesperonychus elizabethae": "хеспероникус елизабетае",
    "dromaeosauridae": "дромаеосауридае",
    "bien élevé": "бјен елеве",
    "panthera": "пантера",
    "fire of anatolia": "фајр оф анатолија",
    "wned buffalo": "дабл ју ен ди бафало",
    "reading rainbow's": "ридинг реинбоус",
    "six flags st louis": "сикс флегс сен луиј",
    "república dominicana": "република доминикана",
    "audition": "одишн",
    "the fools who dream": "д фулс ху дрим",
    "city of stars": "сити оф старс",
    "medecins sans frontieres": "медецинс санс фрoнтиерес",
    "our dumb world": "аур дам ворлд",
    "craigslist": "крегслист",
    "kriegsmarine": "кригсмарин",
    "grachtengordel": "грахтенгордел",
    "николас алден 25 г": "николас алден дваесет и пет години",
    "захари кадбек 21г": "дваесет и една година",
    "[серијата]": "серијата",
    "star alliance": "стар алајанс",
    "latam oneworld": "латам уанворлд",
    "б&б": "би ен би",
    "revolution": "револушн",
    "nintendo": "нинтендо",
    "iphone": "ајфон",
    "apple": "епл",
    "yahoo": "јаху",
    "microsoft": "микрософт",
    "aol": "еј о ел",
    "skype": "скајп",
    "asus": "асус",
    "ebay": "ибеј",
    "myspace": "мајспејс",
    "3,000 милји": "3 илјади милји",
    "во 1979": "во илјада деветстотини седумдесет и деветта",
    "5 $ и 100 $": "пет долари и сто долари",
    "$1000": "илјада долари",
    "u-boats": "ју боутс",
    "asociacion argentina de polo": "асоцијацион аргентина де поло",
    "1492 и 1498": "илјада четиристотини деведесет и втора и илјада четиристотини деведесет и осма",
    "m16-пушка": "ем шеснаесет пушка",
    "sanparks": "санпаркс",
    "usa gymnastics": "ју ас еј џимнастикс",
    "mинистер": "министер",
    "office": "офис",
    "nextgen": "некстген",
    "802.11а": "осумстотини и два точка единаесет ej",
    "802.11b": "осумстотини и два точка единаесет би",
    "802.11g": "осумстотини и два точка единаесет џи",
    "802.11n": "осумстотини и два точка единаесет ен",
    "802,11n": "осумстотини и два запирка единаесет ен",
    "kv62": "кеј ви сиксти ту",
    "елизабета ii": "елизабета втора",
    "1970-ите": "илјада деветстотини седумсеттите",
    "1-та и 3-та": "првата и третата",
    "25-те": "дваесет и петтe",
    "1850-те": "1850-тите",
    "15-от": "15-тиот",
    "18-от": "18-тиот",
    "19-от": "19-тиот",
    "8 век": "осмиот век",
    "1894-1895": "1894-та 1895-та",
    "4,2-3,9": "4,2 до 3,9",
    "35-40": "од 35 до 40",
    "56-64": "од 56 до 64",
    "1.000-та": "1000-та",
    "9.000-": "9000 ",
    "1418-1450": "од 1418-та до 1450-та",
    "1000 - 1300": "од 1000-та до 1300",
    "1644-1912": "од 1644-та до 1912",
    "1995-96": "1995-та 96",
    "1200-те": "илјада и двестоте",
    "78-те": "седумдесет и осумте",
    "100-200": "100 до 200",
    "милји/час": "милји на час",
    "116-те": "сто и шеснаесетте",
    "1/5 инчи": "една петина инчи",
    "на пр.": "на пример",
    "пр н е": "пред нашата ера",
    "larson and lafasto 1989 p109": "ларсон енд лафасто илјада деветстотини осумдесет и деветта пи сто и девет",
    "бр 11": "број единаесет",
    "xdr-tb": "икс де ар тебе",
    "zmapp": "зи мап",
    "ah5n1": "а ха пет ен еден",
    "h5n1": "ха пет ен еден",
    "nhc": "ен ха це",
    "http": "ха те те пе",
    "add": "адеде",
    "acma": "асма",
    " км² ": " километри квадратни ",
    "10:00": "десет",
    "10:08": "десет и осум",
    "11:00": "единаесет",
    "8:46": "8 и 46",
    "над +30": "над плус 30",
    "од 1977 до": "од 1977-ма до",
    "д-р": "доктор",
    "г-дин": "господин",
    "г-ѓа ": "госпоѓа",
    "цг4684": "ц г 4 6 8 4",
    "12.00 gmt": "12 џи ем ти",
    "9:30 am": "9 и 30 еј ем",
    "2:30 utc": "2 и 30 јутиси",
    "07:19 ч.": "7 и 19 часот",
    "09:19 ч.": "9 и 19 часот",
    "т.е.": "то ест",
    "слика 1.1": "слика 1 точка 1",
    " mbit/s": " мегабити на секунда",
    "r и rr": "ар и ар ар",
    " % ": " проценти ",
    "caro": "каро",
    "carro": "каро",
    "г н.е": "година од нашата ера",
    "г н.е.": "година од нашата ера",
    "п.н.е": "пред нашата ера",
    "cctv": "сиситиви",
    "toto": "тото",
    "rem": "рем",
    "npws": "ен пи даблју ес",
    "хемиска ph": "хемиска пеха",
    "нивото на ph": "нивото на пеха",
    "јони h во ph": "јони ха во пеха",
    "tmz": "ти ем зи",
    "dvd": "ди ви ди",
    "usgs": "ју ес џи ес",
    "rspca": "ар ес пи си еј",
    "се`": "се",
    "pstn": "пи ес ти ен",
    "783,562": "783562",
    "300,948": "300948",
    "755,688": "755688",
    "291,773": "291773",
    "23,764": "23764",
    "9,174": "9174",
    "2,243": "2243",
    "$2,3 милијарди": "два запирка три милијарди долари",
    "gps": "џипиес",
    "буквата v": "буквата в",
    "õ/õ": "о",
    "pbs": "пибиес",
    "аполо x": "аполо 10",
    "во 2003": "во 2003-та",
    "minae": "минае",
    "genus": "генус",
    "vpn": "випиен",
    "james et al. 1995": "џејмс ет ал 1995-та",
    "aps": "еј пи ес",
    "ip": "ајпи",
    "лиалофи iii": "лиалофи третиот",
    "ftir": "еф ти ај ар",
    "wifi": "вај фај",
    "35° w": "35 степени западно",
    "11 000": "11000",
    "4892 м": "4892 метри",
    "22 500": "22500",
    "1920тите": "1920-тите",
    "1,400": "1400",
    "во 2010 ": "во 2010-та",
    "од 2008": "од 2008-ма",
    "dslr": "ди ес ел ар",
    " km2 ": " километри квадратни ",
    " km ": " километри ",
    "2,4 ghz и 5,0 ghz": "два запирка четири гигахерци и пет запирка нула гигахерци",
    " км ": " километри ",
    " sq mi ": " сквар мил ",
    " mph": " милји на час",
    " ми/ч": " милји на час",
    " km/h": " километри на час",
    " kph": " километри на час",
    " км/ч": " километри на час",
    " cm": " сентиметри",
    " мм": " милиметри",
    "30,000": "30000",
    "¥2.500": "2500 јени",
    "23:35 ч": "23 и 35 часот",
    "40 000": "40000",
    "¥130.000": "130000 јени",
    "¥7.000": "7000 јени",
    "it month": "ајти мант",
    " mm": " милиметри",
    "mdt": "емдити",
    "palm": "палм",
    'c" и g"': "це и ге",
    "1469-1539": "од 1469-та до 1539-та",
    "90°f": "90 степени фаренхајтови",
    "overscan": "оверскен",
    "jas": "јас",
    "qvc": "кјувиси",
    "callejon del beso": "калехон дел бесо",
    "sie": "зи",
    "луј xvi": "луј шеснаесетти",
    "¾": " и три четвртини",
    "½": " и една половина",
    "ѝ": "и",
    "ѐ": "е",
    "è": "е",
}

POST_REPLACEMENT_PATTERNS = {
    '"': "",
    ".": "",
    ":": " ",
    "-": " ",
    "—": " ",
    "'": "",
    "/": " ",
    ";": "",
    "!": "",
    ",": "",
    "]": "",
    "[": "",
    "~": "",
    "a": "а",
    "c": "с",
    "e": "е",
    "i": "и",
    "j": "ј",
    "o": "о",
    "s": "ѕ",
}

process = Pipeline(
    [
        Replacer(REPLACEMENT_PATTERNS),
        dates2words,
        ordinal2words,
        cardinals2words,
        Replacer(POST_REPLACEMENT_PATTERNS),
    ]
)