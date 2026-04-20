import Logo from './logo'

const Header = () => 
{

return(

 <div className="navbar">
        <ul className="nav">
            <Logo />
            <span className ='name'><a href=""> Hacker News </a></span>

            <li className="nav-li new">new</li>
            <li className="nav-li">past</li>
            <li className="nav-li">comments</li>
            <li className="nav-li">ask</li>
            <li className="nav-li">show</li>
            <li className="nav-li">jobs</li>
            <li className="nav-li">submit</li>

            <span className ='login'><a href="">login</a></span>

        </ul>
 </div>

);

};

export default Header;