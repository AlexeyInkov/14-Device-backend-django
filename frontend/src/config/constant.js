const debug = true
export const BASENAME = ''; // не добавляйте '/' в конце BASENAME
export const BASE_URL = '/app/dashboard/default';
export const BASE_TITLE = ' | React Datta Able ';
export const API_SERVER = (!debug ? '/api' : 'http://127.0.0.1:8000');
console.log(API_SERVER);
export const URL_MENU = '/v1/page/menu/';
export const URL_ADDRESSES = '/v1/page/addresses/';
export const URL_DEVICES = '/v1/page/devices/';
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