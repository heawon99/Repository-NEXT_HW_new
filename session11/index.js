     const title1 =document.getElementById('title');
     
     title1.innerHTML= '합격축하한다' ;
     title.style.color ='red';

     const divs =document.querySelectorAll('div');
     for ( let i =0; i <divs.length; i++) {
        //  divs[i].style.width ='100%' ;
        //  divs[i].style.height ='100px' ;
        //  divs[i].style.fontSize = '${(i+1) * 10}px';
        console.log(divs[i]);
        currntDiv.style.width ='100%';
        currntDiv.style.height ='100px';
        currntDiv.style.fontSize ='${(i+1) * 10}px';
        currntDiv.style.innerHTML ='${i}번째 div';
                

     }

   

    //  const titleLength = title.title.length;


    //  if (titleLength > 20) {
    //      title.style.color ='red';
    //     } else {
    //             title.style.color ='orange'
    //     }

    //     titleLength >20
    //     ? (title.style.color = 'red')
    //     : (title.style.color = 'blue');

    //  console.log(title);
    //  const subTitle =title.querySelector('#title1');
    //  console.log(subTitle);
     
   
