import '../../styles/header.css';
import HeaderLoginForm from "./header_login_form.jsx";
// import Header_login_form from "./header_login_form";
// import HeaderLoginForm from "./header_login_form";

function Header(props) {
    return (
        <header>
            <div>Контроль поверок приборов</div>
            <nav className="navigat">
                <div>ЗАО НТО ГАЛАКС</div>
                <div>{props.userData ? props.userData.username : <HeaderLoginForm setUserData={props.setUserData}/>}</div>
            </nav>
        </header>);
}

export default Header;