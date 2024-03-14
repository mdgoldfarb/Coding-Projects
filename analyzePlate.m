function [avgTemp, maxChangePoint,diff] = analyzePlate(initialPlate, plate)
%ANALYZEPLATE Summary of this function goes here
%This function finds the average temperature of the plate after updating it
%many times until the maximum temp change is less than .01. It also finds
%the index of the maximum change in temperature from the original to the
%newest version of the plate. 
%
%   Detailed explanation goes here
%The functions "mean" and "find" help when finding the average of all the
%values in a matrix, as well as finding a certain index of the highest
%value, I also used a "diff" variable to make a new matrix and the "max"
%function to find the variable of the matrix of differences

avgTemp=mean(plate(:));%function that computes the average temperature
diff=abs(initialPlate-plate); %a function to make the matrix of the difference in temperatures using absolute values to keep it from being negative
maxChangePoint=find(diff == max(diff(:))); %the find function finds the index with the highest change in temperature
end

