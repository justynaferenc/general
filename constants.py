# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:53:32 2024

@author: jferenc
"""

COUNTRY_CODES = {
    "ANDORRA": "AD",
    "UNITED ARAB EMIRATES": "AE",
    "AFGHANISTAN": "AF",
    "ANTIGUA AND BARBUDA": "AG",
    "ANGUILLA": "AI",
    "ALBANIA": "AL",
    "ARMENIA": "AM",
    "ANGOLA": "AO",
    "ANTARCTICA": "AQ",
    "ARGENTINA": "AR",
    "AMERICAN SAMOA": "AS",
    "AUSTRIA": "AT",
    "AUSTRALIA": "AU",
    "ARUBA": "AW",
    "ÅLAND ISLANDS": "AX",
    "AZERBAIJAN": "AZ",
    "BOSNIA AND HERZEGOVINA": "BA",
    "BARBADOS": "BB",
    "BANGLADESH": "BD",
    "BELGIUM": "BE",
    "BURKINA FASO": "BF",
    "BULGARIA": "BG",
    "BAHRAIN": "BH",
    "BURUNDI": "BI",
    "BENIN": "BJ",
    "SAINT BARTHÉLEMY": "BL",
    "BERMUDA": "BM",
    "BRUNEI DARUSSALAM": "BN",
    "BOLIVIA (PLURINATIONAL STATE OF)": "BO",
    "BONAIRE, SINT EUSTATIUS AND SABA": "BQ",
    "BRAZIL": "BR",
    "BAHAMAS": "BS",
    "BHUTAN": "BT",
    "BOUVET ISLAND": "BV",
    "BOTSWANA": "BW",
    "BELARUS": "BY",
    "BELIZE": "BZ",
    "CANADA": "CA",
    "COCOS (KEELING) ISLANDS": "CC",
    "CONGO, DEMOCRATIC REPUBLIC OF THE": "CD",
    "CENTRAL AFRICAN REPUBLIC": "CF",
    "CONGO": "CG",
    "SWITZERLAND": "CH",
    "CÔTE D'IVOIRE": "CI",
    "COOK ISLANDS": "CK",
    "CHILE": "CL",
    "CAMEROON": "CM",
    "CHINA": "CN",
    "COLOMBIA": "CO",
    "COSTA RICA": "CR",
    "CUBA": "CU",
    "CABO VERDE": "CV",
    "CURAÇAO": "CW",
    "CHRISTMAS ISLAND": "CX",
    "CYPRUS": "CY",
    "CZECH REPUBLIC": "CZ",
    "GERMANY": "DE",
    "DJIBOUTI": "DJ",
    "DENMARK": "DK",
    "DOMINICA": "DM",
    "DOMINICAN REPUBLIC": "DO",
    "ALGERIA": "DZ",
    "ECUADOR": "EC",
    "ESTONIA": "EE",
    "EGYPT": "EG",
    "WESTERN SAHARA": "EH",
    "ERITREA": "ER",
    "SPAIN": "ES",
    "ETHIOPIA": "ET",
    "FINLAND": "FI",
    "FIJI": "FJ",
    "FALKLAND ISLANDS (MALVINAS)": "FK",
    "MICRONESIA (FEDERATED STATES OF)": "FM",
    "FAROE ISLANDS": "FO",
    "FRANCE": "FR",
    "GABON": "GA",
    "UNITED KINGDOM": "GB",
    "GRENADA": "GD",
    "GEORGIA": "GE",
    "FRENCH GUIANA": "GF",
    "GUERNSEY": "GG",
    "GHANA": "GH",
    "GIBRALTAR": "GI",
    "GREENLAND": "GL",
    "GAMBIA": "GM",
    "GUINEA": "GN",
    "GUADELOUPE": "GP",
    "EQUATORIAL GUINEA": "GQ",
    "GREECE": "GR",
    "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS": "GS",
    "GUATEMALA": "GT",
    "GUAM": "GU",
    "GUINEA-BISSAU": "GW",
    "GUYANA": "GY",
    "HONG KONG": "HK",
    "HEARD ISLAND AND MCDONALD ISLANDS": "HM",
    "HONDURAS": "HN",
    "CROATIA": "HR",
    "HAITI": "HT",
    "HUNGARY": "HU",
    "INDONESIA": "ID",
    "IRELAND": "IE",
    "ISRAEL": "IL",
    "ISLE OF MAN": "IM",
    "INDIA": "IN",
    "BRITISH INDIAN OCEAN TERRITORY": "IO",
    "IRAQ": "IQ",
    "IRAN (ISLAMIC REPUBLIC OF)": "IR",
    "ICELAND": "IS",
    "ITALY": "IT",
    "JERSEY": "JE",
    "JAMAICA": "JM",
    "JORDAN": "JO",
    "JAPAN": "JP",
    "KENYA": "KE",
    "KYRGYZSTAN": "KG",
    "CAMBODIA": "KH",
    "KIRIBATI": "KI",
    "COMOROS": "KM",
    "SAINT KITTS AND NEVIS": "KN",
    "KOREA (DEMOCRATIC PEOPLE'S REPUBLIC OF)": "KP",
    "KOREA, REPUBLIC OF": "KR",
    "KUWAIT": "KW",
    "CAYMAN ISLANDS": "KY",
    "KAZAKHSTAN": "KZ",
    "LAO PEOPLE'S DEMOCRATIC REPUBLIC": "LA",
    "LEBANON": "LB",
    "SAINT LUCIA": "LC",
    "LIECHTENSTEIN": "LI",
    "SRI LANKA": "LK",
    "LIBERIA": "LR",
    "LESOTHO": "LS",
    "LITHUANIA": "LT",
    "LUXEMBOURG": "LU",
    "LATVIA": "LV",
    "LIBYA": "LY",
    "MOROCCO": "MA",
    "MONACO": "MC",
    "MOLDOVA, REPUBLIC OF": "MD",
    "MONTENEGRO": "ME",
    "SAINT MARTIN (FRENCH PART)": "MF",
    "MADAGASCAR": "MG",
    "MARSHALL ISLANDS": "MH",
    "NORTH MACEDONIA": "MK",
    "MALI": "ML",
    "MYANMAR": "MM",
    "MONGOLIA": "MN",
    "MACAO": "MO",
    "NORTHERN MARIANA ISLANDS": "MP",
    "MARTINIQUE": "MQ",
    "MAURITANIA": "MR",
    "MONTSERRAT": "MS",
    "MALTA": "MT",
    "MAURITIUS": "MU",
    "MALDIVES": "MV",
    "MALAWI": "MW",
    "MEXICO": "MX",
    "MALAYSIA": "MY",
    "MOZAMBIQUE": "MZ",
    "NAMIBIA": "NA",
    "NEW CALEDONIA": "NC",
    "NIGER": "NE",
    "NORFOLK ISLAND": "NF",
    "NIGERIA": "NG",
    "NICARAGUA": "NI",
    "NETHERLANDS": "NL",
    "NORWAY": "NO",
    "NEPAL": "NP",
    "NAURU": "NR",
    "NIUE": "NU",
    "NEW ZEALAND": "NZ",
    "OMAN": "OM",
    "PANAMA": "PA",
    "PERU": "PE",
    "FRENCH POLYNESIA": "PF",
    "PAPUA NEW GUINEA": "PG",
    "PHILIPPINES": "PH",
    "PAKISTAN": "PK",
    "POLAND": "PL",
    "SAINT PIERRE AND MIQUELON": "PM",
    "PITCAIRN": "PN",
    "PUERTO RICO": "PR",
    "PALESTINE, STATE OF": "PS",
    "PORTUGAL": "PT",
    "PALAU": "PW",
    "PARAGUAY": "PY",
    "QATAR": "QA",
    "RÉUNION": "RE",
    "ROMANIA": "RO",
    "SERBIA": "RS",
    "RUSSIAN FEDERATION": "RU",
    "RWANDA": "RW",
    "SAUDI ARABIA": "SA",
    "SOLOMON ISLANDS": "SB",
    "SEYCHELLES": "SC",
    "SUDAN": "SD",
    "SWEDEN": "SE",
    "SINGAPORE": "SG",
    "SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA": "SH",
    "SLOVENIA": "SI",
    "SVALBARD AND JAN MAYEN": "SJ",
    "SLOVAKIA": "SK",
    "SIERRA LEONE": "SL",
    "SAN MARINO": "SM",
    "SENEGAL": "SN",
    "SOMALIA": "SO",
    "SURINAME": "SR",
    "SOUTH SUDAN": "SS",
    "SAO TOME AND PRINCIPE": "ST",
    "EL SALVADOR": "SV",
    "SINT MAARTEN (DUTCH PART)": "SX",
    "SYRIAN ARAB REPUBLIC": "SY",
    "ESWATINI": "SZ",
    "TURKS AND CAICOS ISLANDS": "TC",
    "CHAD": "TD",
    "FRENCH SOUTHERN TERRITORIES": "TF",
    "TOGO": "TG",
    "THAILAND": "TH",
    "TAJIKISTAN": "TJ",
    "TOKELAU": "TK",
    "TIMOR-LESTE": "TL",
    "TURKMENISTAN": "TM",
    "TUNISIA": "TN",
    "TONGA": "TO",
    "TÜRKIYE": "TR",
    "TRINIDAD AND TOBAGO": "TT",
    "TUVALU": "TV",
    "TAIWAN PROVINCE OF CHINA": "TW",
    "TANZANIA, UNITED REPUBLIC OF": "TZ",
    "UKRAINE": "UA",
    "UGANDA": "UG",
    "UNITED STATES MINOR OUTLYING ISLANDS": "UM",
    "UNITED STATES": "US",
    "URUGUAY": "UY",
    "UZBEKISTAN": "UZ",
    "HOLY SEE": "VA",
    "SAINT VINCENT AND THE GRENADINES": "VC",
    "VENEZUELA (BOLIVARIAN REPUBLIC OF)": "VE",
    "VIRGIN ISLANDS (BRITISH)": "VG",
    "VIRGIN ISLANDS (U.S.)": "VI",
    "VIET NAM": "VN",
    "VANUATU": "VU",
    "WALLIS AND FUTUNA": "WF",
    "SAMOA": "WS",
    "YEMEN": "YE",
    "MAYOTTE": "YT",
    "SOUTH AFRICA": "ZA",
    "ZAMBIA": "ZM",
    "ZIMBABWE": "ZW",
    }
