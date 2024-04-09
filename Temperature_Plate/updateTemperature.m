function updatedPlate = updateTemperature(plate)
%UPDATETEMPERATURE Summary of this function goes here
%This function updates the temperature for each inner square by averaging
%the 4 neighbors and making the average its new value
%
%   Detailed explanation goes here
%Just like the first function, the output value is a plate, but it is
%updated after 1 iteration of average values. It uses 2 for loops that are
%nested just like the original function and if its a corner or edge, it is
%kept at the SAME temperature, if it is not, it is the average of its
%neighbor of (i,j+1), etc. The new plate will be conducted in this loop
%with the input value of the plate from the initialzePlate function, the
%output value is the updated plate after 1 iteration. 

updatedPlate=zeros(size(plate,1),size(plate,2));%make another plate the same size as the initial plate
for i=1:size(plate,1)%The same nested for loops for the sizes
    for j=1:size(plate,2)
        if i~=1 && j~=1 && i~=size(plate,1) && j~=size(plate,2)
            updatedPlate(i,j)= (plate(i-1,j)+plate(i,j-1)+plate(i,j+1)+plate(i+1,j))/4;%computes the average temperature for those indicides in the center and NOT on the edges
        end
        if i==1 || j==1 || i==size(plate,1) || j == size(plate,2) %This condition keeps the edges the same
            updatedPlate(i,j)=plate(i,j);
        end
    end 
end 
            
            