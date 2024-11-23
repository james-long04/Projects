#include <stdio.h>

#define ROW 10
#define COL 10

int main()
{
    int p1[ROW][COL] = {0};
    int p2[ROW][COL] = {0};
    int i,x,y,z,j,p;

    printf("Welcome to battleships!\n");
    printf("Player 1\n");
    printf("Enter where you want your three ships to be placed\n");
    printf("Enter the coordinantes of your scout (2 spaces long)\n");
    for (i=0; i < 2; i++)
    {
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);
        // they must be connecting horizontally, vertically or diagonally
        p1[x][y] = 1;
    }
    printf("Enter the coordinantes of your cruiser (4 spaces long)\n");
    for (i=0; i < 4; i++)
    {
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);
        // they must be connecting horizontally, vertically or diagonally
        p1[x][y] = 1;
    }
    printf("Enter the coordinantes of your battleship (5 spaces long)\n");
    for (i=0; i < 5; i++)
    {
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);
        // they must be connecting horizontally, vertically or diagonally
        p1[x][y] = 1;
    }
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("/************/");
    printf("Player 2\n");
    printf("Enter where you want your three ships to be placed\n");
    printf("Enter the coordinantes of your scout (2 spaces long)\n");
    for (i=0; i < 2; i++)
    {
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);
        // they must be connecting horizontally, vertically or diagonally
        p2[x][y] = 1;
    }
    printf("Enter the coordinantes of your cruiser (4 spaces long)\n");
    for (i=0; i < 4; i++)
    {
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);
        // they must be connecting horizontally, vertically or diagonally
        p2[x][y] = 1;
    }
    printf("Enter the coordinantes of your battleship (5 spaces long)\n");
    for (i=0; i < 5; i++)
    {
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);
        // they must be connecting horizontally, vertically or diagonally
        p2[x][y] = 1;
    }

    while (z != 1)
    {
        printf("Player 1, please enter your guess\n");
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);

        if (p2[x][y] == 0)
        {
            printf("Miss!\n");   
        }

        if (p2[x][y] == 1)
        {
            printf("Hit!\n");
            p2[x][y] = 0;    
        }
        //player 2 time to shine
        printf("Player 2, please enter your guess\n");
        printf("Please enter row\n");
        scanf("%d", & x);
        printf("Please enter col\n");
        scanf("%d", & y);

        if (p1[x][y] == 0)
        {
            printf("Miss!\n");   
        }

        if (p1[x][y] == 1)
        {
            printf("Hit!\n");
            p1[x][y] = 0;    
        }

        for(i = 0; i < ROW; i++)
 	    {
   		// Inner for that handles the Cols
   		    for(j = 0; j < COL; j++)
   		    {
     		// display the data
     		    if (p1[i][j] == 0)
                {
                    p+=1;
                }
   		    } // end inner for
 	    } // end outer for

        if (p == 100)
        {
            printf("Congrats player 1!\n");
            printf("You win!\n");
            z = 1;
        }
        p=0;

        //player 2 time
        for(i = 0; i < ROW; i++)
 	    {
   		// Inner for that handles the Cols
   		    for(j = 0; j < COL; j++)
   		    {
     		// display the data
     		    if (p2[i][j] == 0)
                {
                    p+=1;
                }
   		    } // end inner for
 	    } // end outer for

        if (p == 100)
        {
            printf("Congrats player 1!\n");
            printf("You win!\n");
            z = 1;
        }
        p=0;
    }

    return 0;
}