import '../styles/menu_filter.css';
const MenuFilter = (props) => {
    const {title,} = props
    return (<div className="menu">{title}</div>);
};

export default MenuFilter;