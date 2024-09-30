export const BASENAME = ''; // не добавляйте '/' в конце BASENAME
export const BASE_URL = '/app/dashboard/default';
export const BASE_TITLE = ' | React Datta Able ';
export const API_SERVER = 'http://127.0.0.1:8000/api';
export const URL_MENU = 'http://127.0.0.1:8000/api/page/menu/';
export const URL_ADDRESSES = 'http://127.0.0.1:8000/api/page/addresses/';
export const URL_DEVICES = 'http://127.0.0.1:8000/api/page/devices/';
export const HEADERS_ADDRESS = {
    'id': '№ п/п',
    'customer': 'Абонент',
    'address': 'Адрес',
    'itp': 'ИТП',
    'tso': 'Теплоснабжающая организация',
    'service_organization': 'Обслуживающая организация'
}
export const HEADERS_DEVICE = {
    'id': '№ п/п',
    'installation_point': 'Место установки',
    'type_of_file': 'Тип',
    'factory_number': 'Зав. №'
}
export const HEADERS_VERIFICATION = {
    "id": '№ п/п',
    "organization": "Поверитель",
    "verification_date": "Дата поверки",
    "valid_date": "Поверка до",
    "is_actual": "Актуальна",
    "is_delete": "Будет удалена"
}