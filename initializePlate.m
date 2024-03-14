function plate = initializePlate(n)
%INITIALIZEPLATE Summary of this function goes here:
%This function creates a new plate that is nxn with certain temperature
%values on certain sides and places and corners
%   Detailed explanation goes here:
%two for loops are created with i and j and it has all the conditions where
%if i is 1 and j is n, etc for the corners and edges, and the center is all
%the same value (25), the sides are 0, 50, 75, and 100 and the corners are
%the average value of their 2 neighboring points. The input is the "n"
%value which helps makes the size of the plate and the output value is
%"plate" which returns the nxn plate with the values.

plate=zeros(n,n);%make the plate size nxn zeros
for i=1:n %2 for loops in range of 1 to size n
    for j=1:n
        if i==1 && j==1 %conditions for the borders of the matrix
            plate(i,j)=50;%First corner is (100+0)/2
        end
        if i==1 && j~=1 && j~=n
            plate(i,j)=100; %upper border is 100 degrees
        end 
        if i==1 && j==n
            plate(i,j)=87.5; %second corner is (100+75)/2
        end 
        if j==n && i~=1 && i~=n
            plate(i,j)=75; %right border
        end 
        if i==n && j==n
            plate(i,j)=62.5;%bottom right borner (75+50)/2
        end 
        if i==n && j~=n && j~=1
            plate(i,j)=50;%lower border
        end 
        if i==n && j==1
            plate(i,j)=25; %all indicies that are not on the edge being 25
        end 
        if i~=1 && i~=n && j==1 %left border
            plate(i,j)=0;
        end 
        if i~=1 && i~=n && j~=1 && j~=n %lower left corner is 50/2
            plate(i,j)=25;
        end
    end
end

        
            