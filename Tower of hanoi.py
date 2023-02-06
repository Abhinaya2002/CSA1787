move(1, A, B,_) :-  
    write('move top disk from'),  
write(A),  
write(' to '),  
write(B),  
p1.  
move(P, A, B, C) :-  
    P>1,  
    S is P-1,  
    move(S, A, B, C),  
    move(1, A, B,_),  
    move(S, C, B, A).  


?- move(3, left, right, center).  
From left to right move top disk   
From left to center move top disk  
From right to center move top disk  
From left to right move top disk  
From center to left move top disk  
From center to right move top disk  
From left to right move top disk  

yes  


move(3,left,right,center) if  

            move(2,left,center,right) and ] *  
            move(1,left,right,center) and  
            move(2,center,right,left). ] ** 

In order to satisfy the goal ?- move(3,left,right,center) do this :  

              satisfy the goal ?-move(2,left,center,right), and then  
              satisfy the goal ?-move(1,left,right,center), and then  
              satisfy the goal ?-move(2,center,right,left).  

move(2,left,center,right) if ] *  

             move(1,left,right,center) and  
             move(1,left,center,right) and  
             move(1,right,center,left).  
move(2,center,right,left) if ] **  

             move(1,center,left,right) and  
             move(1,center,right,left) and  
             move(1,left,right,center).  


move(3,left,right,center) if  

        move(1,left,right,center) and  
        move(1,left,center,right) and *  
        move(1,right,center,left) and  
        ---------------------------  
        move(1,left,right,center) and  
         ---------------------------  
        move(1,center,left,right) and  
        move(1,center,right,left) and **  
        move(1,left,right,center).  
