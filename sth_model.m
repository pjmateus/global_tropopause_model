function z = sth_model(lat, doy, pvu)
% Sigmoid-model for tropopause height determination
% INPUT
%       lat : latitude, in degrees [-90..90]  (can be an array)
%       doy : day-of-year          [1..366]   (can be an array, same size as lat)
%       pvu : PVU value            [1.5..3.5] 
%
% OUTPUT
%       z   : tropopause height, in km
% 
% For details see:
% Global empirical models for tropopause height determination
% Pedro Mateus, Virgílio B. Mendes, and Carlos A.L. Pires
% Instituto Dom Luiz, Faculdade de Ciências, Universidade de Lisboa, Lisbon, Portugal
% pjmateus@fc.ul.pt; vmendes@fc.ul.pt; clpires@fc.ul.pt
% Submitted to Atmospheric Research Journal
%
if nargin < 3
    pvu = 3.5;
    disp('Fixing the PVU in 3.5!')
elseif nargin < 2
    error('Not enough input arguments!')
end
if pvu < 1.5 || pvu > 3.5
    disp('Extrapolation, use with care!')
end
if size(lat,2) > 1, lat = lat'; end
if size(doy,2) > 1, doy = doy'; end

z = nan(length(lat),1);
for i = 1 : length(lat)
    if lat(i) <=0
        % SH
        %   a_0	    a_1	    a_2	      a_3	  a_4	  a_5      pvu
        a =[7.2086, 9.1185, -18.9363, 1.8065, 0.1067, -0.1859; % 1.5
            7.7749, 8.5516, -21.3633, 1.3565, 0.0879, -0.1640; % 2.0
            8.1797, 8.1455, -23.4839, 1.1464, 0.0798, -0.1491; % 2.5
            8.5055, 7.8175, -25.3146, 1.1133, 0.0819, -0.1370; % 3.0
            8.7796, 7.5417, -26.7300, 1.1474, 0.0870, -0.1255];% 3.5
    else
        % NH
        %   a_0	    a_1	    a_2	      a_3	  a_4	  a_5      pvu
        a =[7.1454, 9.1847, 20.1173, -2.8115, 0.1509, -0.1863; % 1.5
            7.6501, 8.6773, 22.4300, -2.3154, 0.1334, -0.1642; % 2.0
            7.9925, 8.3329, 24.1731, -1.8069, 0.1082, -0.1493; % 2.5
            8.2649, 8.0584, 25.5622, -1.5508, 0.0950, -0.1372; % 3.0
            8.4990, 7.8229, 26.7284, -1.5804, 0.0980, -0.1257];% 3.5
    end       
    a0 = a(:,1); 
    a1 = a(:,2); 
    a2 = a(:,3); 
    a3 = a(:,4); 
    a4 = a(:,5); 
    a5 = a(:,6);
    d = (1+exp(-(lat(i)-a2)./a3)).^a4;
    arg = 2*pi/365.25 .* (doy(i)-28);
    z_ = a0 + a1./d + a5 .* cos(arg);
    if pvu == 3.5
        z(i) = z_(end);
    else
        p = polyfit((1.5:0.5:3.5), z_', 1);
        z(i) = polyval(p, pvu);
    end
end
return