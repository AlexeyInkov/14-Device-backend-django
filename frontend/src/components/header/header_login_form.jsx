
import TextInput from "../text_input";

const HeaderLoginForm = () => {
    return (
        <>
            <TextInput type="text" placeholder="login:"/>
            <TextInput type="password" placeholder="password:"/>
            <input type={"button"} value={"login"} />
        </>
    );
};

export default HeaderLoginForm;