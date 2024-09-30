import {URL_MENU} from "../config/constant.js";

export async function fetchMenu() {

    const res = await fetch(URL_MENU)

    if (!res.ok) throw new Error('Failed to fetch menu!')

    return res.json()
}