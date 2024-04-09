% Initialize the plate
n = 50; % Size of the plate
plate = initializePlate(n);
% Visualize and save the initial temperature distribution
figure;
imagesc(plate);
colorbar;
title('Initial Temperature Distribution');
saveas(gcf, 'initial_temperature.png');
% Iteratively update the temperature distribution
threshold = 0.01;
maxChange = Inf;
initialPlate = plate;
iteration = 0;
% For movie creation
F(n) = struct('cdata',[],'colormap',[]);
while maxChange > threshold
updatedPlate = updateTemperature(plate);
maxChange = max(max(abs(updatedPlate - plate)));
plate = updatedPlate;
iteration = iteration + 1;
% Visualize the current temperature distribution
imagesc(plate);
title(['Iteration ', num2str(iteration)]);
% For movie creation
F(iteration) = getframe(gcf);
end
% Save the movie in MP4 format
v = VideoWriter('temperature_evolution', 'MPEG-4'); % Specify MPEG-4 format
v.Quality = 95; % Set quality (0-100). Higher value gives better quality.
v.FrameRate = 10; % Set frame rate. Adjust as needed.
open(v);
writeVideo(v, F);
close(v);
% Analyze the plate
[avgTemp, maxChangePoint] = analyzePlate(initialPlate, plate);
% Plot the temperature distribution along the diagonal
figure;
plot(diag(plate));
title('Temperature Distribution Along the Diagonal');
xlabel('Position Along Diagonal');
ylabel('Temperature (°C)');
saveas(gcf, 'diagonal_temperature.png');
