//ref: https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/
//implement Knight Tour's problem using Warnsdorff's algorithm
#include<bits/stdc++.h>
using namespace std;

#define N 8

//set of valid moves for Knight on N*N board/cells
int movx[N] = {1,1,2,2,-1,-1,-2,-2};
int movy[N] = {2,-2,1,-1,2,-2,1,-1};

//display the matrix, i.e: the board
void dispmat(int sol[N][N])
{
    for(int row=0; row<N; row++){
        for(int col=0; col<N; col++){
            cout<<" "<<setw(4)<<sol[row][col]<<" ";
        }
        cout<<endl;
    }
}

//finds out if given cell is within the N*N cell and is empty
bool isValid(int sol[N][N], int x, int y)
{
    return (x>=0 && x<N && y>=0 && y<N && sol[x][y] == -1);
}

//finds our what number of adjacent cells of given cells are valid for the next move
int getDegree(int sol[N][N], int x, int y)
{
    int count = 0;

    for(int i=0; i<N; i++){
        if(isValid(sol, x+movx[i], y+movy[i])){
            count++;
        }
    }

    return count;
}

//uses isValid and getDegree to find out the single next move
//uses reference variables to update the position of the Knight
bool findNextMove(int sol[N][N], int &x, int &y)
{
    int nextmoveid = -1, mindeg = N+1, nx, ny, i, c;

    int start = rand()%N;

    for(int count = 0; count < N; count++){
        i = (start + count) % N;
        nx = x + movx[i];
        ny = y + movy[i];
        if(isValid(sol, nx, ny)&&(c = getDegree(sol, nx, ny))<mindeg){
            nextmoveid = i;
            mindeg = c;
        }
    }

    if (nextmoveid == -1)
        return false;

    nx = x + movx[nextmoveid];
    ny = y + movy[nextmoveid];

    sol[nx][ny] = sol[x][y] + 1;

    x = nx;
    y = ny;

    return true;
}

// Check if tour is closed,
//i.e:the end lies adjacent to start in terms of Knight's move
bool isNeighbour(int x, int y, int xx, int yy)
{
    for (int i = 0; i < N; ++i)
        if (((x+movx[i]) == xx)&&((y + movy[i]) == yy))
            return true;

    return false;
}

//loops N*N times to find out a closed path for a new random start point
bool findClosedPath(int sol[N][N])
{
    for(int row=0; row<N; row++)
        for(int col=0; col<N; col++)
            sol[row][col] = -1;

    int sx = rand()%N;
    int sy = rand()%N;

    int x = sx;
    int y = sy;

    sol[x][y] = 1;

    for(int moves=0; moves<N*N-1; moves++)
            if(!findNextMove(sol, x, y)) return false;

    if (!isNeighbour(x, y, sx, sy))
        return false;

    cout<<"The closed path solution is: "<<endl;
    dispmat(sol);

    return true;
}

//keeps looping until a path is found
int main()
{
    srand(time(NULL));

    int sol[N][N];

    while(!findClosedPath(sol)){
        ;
    }

    return 0;
}

