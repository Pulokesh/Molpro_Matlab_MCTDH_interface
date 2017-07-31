%-----------------------------------------------------------
%        Copyright (C) 2017 Ekadashi Pradhan
%-----------------------------------------------------------
%
%% this is for batch job
%% Create 80N folder in the same directory
% loads train test, val set
	load('train');
	load('test');
	load('val');
	%loading;
	% Fitting with 80NN
	HFCO=scaled_onestg(['HFCO'],6,train,test,val,80,0,0.0000000001,0,300,0);
	% saving weights, biases, and errofiles in to the 80N folder
	copyfile ('HFCO.LW','80N/');
	copyfile ('HFCO.IW','80N/');
	copyfile ('HFCO.b','80N/');
	copyfile ('HFCO.c','80N/');
	copyfile ('HFCO.errorfile2','80N/');
	copyfile ('HFCO.errorfile1','80N/');
	clear

%% run this script from commandline as
% matlab -nodisplay <script.m> nohup.out &
% performane can be checked from nohup.out while program is running.
