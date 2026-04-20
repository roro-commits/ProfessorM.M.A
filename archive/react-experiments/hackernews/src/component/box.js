import React from 'react'

function Box ({threads}){

    return(

        <div className="box">
            <div className="thread">
                <span>{threads.id}.</span>

                <span>
                <i class="fa fa-caret-up"></i>
                </span>

               <a href="http://">
               <span className="name">
                    <a href="http://">
                    {threads.thread_name}
                    </a>
                </span>
               </a>
                <span className ='web'>
                    <a href={threads.web} className ='web'>(website)</a>
                </span>

             </div>


            <div className="tags">
                <span className = 'tag'><a href="http://">{threads.stats.point}points </a></span>
                <span className = 'tag border'><a href="http://">{threads.stats.time}</a></span>
                <span className = 'tag border'><a href="http://">{threads.stats.hide}</a></span>
                <span className = 'tag border'><a href="http://"> {threads.stats.time}</a></span>
                <span className = 'tag border'> <a href="http://"> {threads.stats.comments}comments</a></span>

            </div>
        </div>
        
      

    );

};

export default Box;