						#
						#
						#
		#################################################################################
		# Call script: python -i threshold_CCPDv2_Tuning_usingFunctions.py				#
		#	OUTPUTFILE.root dataTDAC.txt data2TDAC.txt .........						#
		#																				#
		# 	Script to plot the threshold distribution from								#
		#	threshold scan																#
		#################################################################################
						#
						#
						#

#=======================================
# --------packages 

import sys
sys.path.insert(0, "/Users/misaelcaloz/Documents/CERN master thesis/python scripts/functions")
sys.path.append("/usr/local/lib/root")
#import ROOT
from ROOT import gROOT, TCanvas, TF1, TGraph, TLegend, TMath, TMultiGraph, TFile, TH2F, TH1F, TDirectory,TH2D, TH1D, TLatex, gPad, TH2I, TLine, TAxis, kTRUE, gStyle, TKey, THStack, kRed, kOrange, kBlue, kGreen
from array import array
import numpy
import math
import pylab
import os
from decimal import Decimal
from functions import *

#------------ input data
#rootFileName=sys.argv[1]

#-------- conversion factor injection -> electrons

#injToElectrons=1660./.25			# WARNING: different depending the version of the chip: v2: 1660/0.39 v4: 1660/0.25

#------------ create file.root

#outFile=TFile(rootFileName,"RECREATE")

# no injection
# data --> pixel: col 24, row 0, probe VS GDAC

grHVCMOSc24r0 = TGraph()
grHVCMOSc24r0.SetPoint(0,0,0.8127)
grHVCMOSc24r0.SetPoint(1,7,0.8339)
grHVCMOSc24r0.SetPoint(2,15,0.8561)
#grHVCMOSc24r0.SetPoint(3,0.795,140)
#grHVCMOSc24r0.SetPoint(4,0.797,50)
#grHVCMOSc24r0.SetPoint(5,0.799,20)
#grHVCMOSc24r0.SetPoint(6,0.8,10)
#grHVCMOSc24r0.SetPoint(7,0.802,5)
#grHVCMOSc24r0.SetPoint(8,0.805,1)
#grHVCMOSc24r0.SetPoint(9,0.81,0)
#grHVCMOSc24r0.SetPoint(10,0.85,0)
#
#
#grFEc24r0 = TGraph()
#grFEc24r0.SetPoint(0,0.79,6058)
#grFEc24r0.SetPoint(1,0.791,4590)
#grFEc24r0.SetPoint(2,0.793,2252)
#grFEc24r0.SetPoint(3,0.795,969)
#grFEc24r0.SetPoint(4,0.797,346)
#grFEc24r0.SetPoint(5,0.799,135)
#grFEc24r0.SetPoint(6,0.8,87)
#grFEc24r0.SetPoint(7,0.805,11)
#grFEc24r0.SetPoint(8,0.81,0)
#grFEc24r0.SetPoint(9,0.85,0)

#myfit=TF1("myfit", "[0]+1/(x^2*[1]-[2])",0.795,0.85)
#myfit.SetParameter(0,-0.1);
#myfit.SetParameter(1,1);
#myfit.SetParameter(2,0.8)
#
#myfit.SetParLimits(0,-0.5,0.5);
#myfit.SetParLimits(1,0.7,1.3);
#myfit.SetParLimits(2,0.7,0.8);

#myfit=TF1("myfit", "exp(-x*[2]+[0])+[1]",0.79,0.82)
##myfit.SetParLimits(0,100,1000);
#myfit.SetParLimits(1,-1,1);
##myfit.SetParLimits(2,100,1000);
#
#
##fa1 = TF1("fa1","exp(-x)/sq(x)",-10,10);
#
#Canvtest = ROOT.TCanvas("Canvtest","CanvGraphC24R0",400,400)
#fa1.Draw();
#gPad.Update()

#myfit=TF1("myfit", "",0.79,0.85)

#
#grHVCMOSc24r0 = TGraph()
#grHVCMOSc24r0.SetPoint(0,0.79,1500)
#grHVCMOSc24r0.SetPoint(1,0.791,800)
#grHVCMOSc24r0.SetPoint(2,0.793,300)
#grHVCMOSc24r0.SetPoint(3,0.795,140)
#grHVCMOSc24r0.SetPoint(4,0.797,50)
#grHVCMOSc24r0.SetPoint(5,0.799,20)
#grHVCMOSc24r0.SetPoint(6,0.8,10)
#grHVCMOSc24r0.SetPoint(7,0.802,5)
#grHVCMOSc24r0.SetPoint(8,0.805,1)
#grHVCMOSc24r0.SetPoint(9,0.81,0)
#grHVCMOSc24r0.SetPoint(10,0.85,0)
#
#
#grFEc24r0 = TGraph()
#grFEc24r0.SetPoint(0,0.79,6058)
#grFEc24r0.SetPoint(1,0.791,4590)
#grFEc24r0.SetPoint(2,0.793,2252)
#grFEc24r0.SetPoint(3,0.795,969)
#grFEc24r0.SetPoint(4,0.797,346)
#grFEc24r0.SetPoint(5,0.799,135)
#grFEc24r0.SetPoint(6,0.8,87)
#grFEc24r0.SetPoint(7,0.805,11)
#grFEc24r0.SetPoint(8,0.81,0)
#grFEc24r0.SetPoint(9,0.85,0)
#


#
#
#
#
#
#
## data --> pixel: col 33, row 6, probe VS GDAC
#
#grHVCMOSc33r6 = TGraph()
#grHVCMOSc33r6.SetPoint(0,0.805,2200)
#grHVCMOSc33r6.SetPoint(1,0.81,1300)
#grHVCMOSc33r6.SetPoint(2,0.811,910)
#grHVCMOSc33r6.SetPoint(3,0.813,400)
#grHVCMOSc33r6.SetPoint(4,0.815,170)
#grHVCMOSc33r6.SetPoint(5,0.817,50)
#grHVCMOSc33r6.SetPoint(6,0.82,30)
#grHVCMOSc33r6.SetPoint(7,0.822,10)
#grHVCMOSc33r6.SetPoint(8,0.825,1)
#grHVCMOSc33r6.SetPoint(9,0.83,0)
#grHVCMOSc33r6.SetPoint(10,0.84,0)


## data --> pixel: col 39, row 9, probe VS GDAC
#
#grHVCMOSc39r9 = TGraph()
#0.805,2000)
#0.81,360)
#0.811,230)
#0.813,90)
#0.815,30)
#0.817,10)
#0.82,2)
#0.822,1)
#0.825,0)
#0.83,0)
#0.84,0)
#
#

#
#
#grHVCMOSc24r0.Fit("myfit","R","B")
#grFEc24r0.Fit("myfit","R","B")



grHVCMOSc24r0.SetLineWidth(2);
grHVCMOSc24r0.SetLineColor(4);
grHVCMOSc24r0.SetMarkerColor(4) # 9 ou 8
grHVCMOSc24r0.SetMarkerSize(0.7);
grHVCMOSc24r0.SetMarkerStyle(21); # 22 ou 33
grHVCMOSc24r0.SetTitle("Pixel row 0 column 24");
grHVCMOSc24r0.GetXaxis().SetTitle("TDAC");
grHVCMOSc24r0.GetYaxis().SetTitle("GDAC [V]");

#grFEc24r0.SetLineWidth(2);
#grFEc24r0.SetLineColor(3);
#grFEc24r0.SetMarkerColor(3) # 9 ou 8
#grFEc24r0.SetMarkerSize(0.7);
#grFEc24r0.SetMarkerStyle(22); # 22 ou 33
#grFEc24r0.SetTitle("Pixel row 0 column 24");
#grFEc24r0.GetXaxis().SetTitle("global threshold [V]");
#grFEc24r0.GetYaxis().SetTitle("probe (128 injections)");
#


CanvGraphC24R0 = ROOT.TCanvas("CanvGraphC24R0","CanvGraphC24R0",400,400)
gStyle.SetOptStat()
grHVCMOSc24r0.Draw("ALP")
#grFEc24r0.Draw("LPsame")

gPad.Update()






ROOT.gApplication.Run()








#
#
#
#
## row 11 col 30 TDAC 7 inj 0.34
#
#GraphWarning = TGraph()
#GraphWarning.SetPoint(0,0.895,2478)
#GraphWarning.SetPoint(1,0.897,268)
#GraphWarning.SetPoint(2,0.899,133)
#GraphWarning.SetPoint(3,0.9,131)
#GraphWarning.SetPoint(4,0.905,128)
#GraphWarning.SetPoint(5,0.91,128)
#GraphWarning.SetPoint(6,0.92,128)
#GraphWarning.SetPoint(7,0.93,128)
#GraphWarning.SetPoint(8,0.94,128)
#GraphWarning.SetPoint(9,0.97,128)
#GraphWarning.SetPoint(10,0.99,128)
#GraphWarning.SetPoint(11,1,128)
#GraphWarning.SetPoint(12,1.01,119)
#GraphWarning.SetPoint(13,1.02,51)
#GraphWarning.SetPoint(14,1.03,10)
#GraphWarning.SetPoint(15,1.04,0)
#GraphWarning.SetPoint(16,1.05,0)
#GraphWarning.SetPoint(17,1.06,0)
#GraphWarning.SetPoint(18,1.1,0)
#
#
#
#Xaxis = GraphWarning.GetXaxis()
#Xaxis.SetLimits(0.8,1.12)
#GraphWarning.GetHistogram().SetMaximum(300.)
#GraphWarning.GetHistogram().SetMinimum(0.)
#
##GraphWarning.Draw("AC*")
#outFile.cd()
#GraphWarning.Write()
#
## row 11 col 30 TDAC 14 inj 0.34
#
#GraphWarning2 = TGraph()
#GraphWarning2.SetPoint(0,0.833,691)
#GraphWarning2.SetPoint(1,0.834,248)
#GraphWarning2.SetPoint(2,0.835,156)
#GraphWarning2.SetPoint(3,0.836,133)
#GraphWarning2.SetPoint(4,0.837,128)
#GraphWarning2.SetPoint(5,0.84,128)
#GraphWarning2.SetPoint(6,0.86,128)
#GraphWarning2.SetPoint(7,0.88,128)
#GraphWarning2.SetPoint(8,0.9,128)
#GraphWarning2.SetPoint(9,0.92,128)
#GraphWarning2.SetPoint(10,0.93,128)
#GraphWarning2.SetPoint(11,0.94,126)
#GraphWarning2.SetPoint(12,0.945,116)
#GraphWarning2.SetPoint(13,0.95,96)
#GraphWarning2.SetPoint(14,0.955,59)
#GraphWarning2.SetPoint(15,0.96,30)
#GraphWarning2.SetPoint(16,0.965,8)
#GraphWarning2.SetPoint(17,0.97,1)
#GraphWarning2.SetPoint(18,0.98,0)
#GraphWarning2.SetPoint(19,0.99,0)
#GraphWarning2.SetPoint(20,1.1,0)
#
#Xaxis = GraphWarning2.GetXaxis()
##Xaxis.SetLimits(0.,16.)
##GraphWarning2.GetHistogram().SetMaximum(2000.)
##GraphWarning2.GetHistogram().SetMinimum(0.)
#
##GraphWarning2.Draw("AC*")
##outFile.cd()
#GraphWarning2.Write()
#
#
## row 11 col 30 TDAC 2 inj 0.34
#
#GraphWarning3 = TGraph()
#GraphWarning3.SetPoint(0,0.93,1573)
#GraphWarning3.SetPoint(1,0.935,129)
#GraphWarning3.SetPoint(2,0.936,128)
#GraphWarning3.SetPoint(3,0.94,128)
#GraphWarning3.SetPoint(4,0.95,128)
#GraphWarning3.SetPoint(5,0.96,128)
#GraphWarning3.SetPoint(6,0.97,128)
#GraphWarning3.SetPoint(7,0.98,128)
#GraphWarning3.SetPoint(8,0.99,128)
#GraphWarning3.SetPoint(9,0.995,128)
#GraphWarning3.SetPoint(10,1,128)
#GraphWarning3.SetPoint(11,1.03,128)
#GraphWarning3.SetPoint(12,1.05,106)
#GraphWarning3.SetPoint(13,1.06,38)
#GraphWarning3.SetPoint(14,1.07,2)
#GraphWarning3.SetPoint(15,1.08,0)
#GraphWarning3.SetPoint(16,1.09,0)
#GraphWarning3.SetPoint(17,1.1,0)
#GraphWarning3.SetPoint(18,1.2,0)
##Xaxis = GraphWarning3.GetXaxis()
##Xaxis.SetLimits(0.,16.)
##GraphWarning3.GetHistogram().SetMaximum(2000.)
##GraphWarning3.GetHistogram().SetMinimum(0.)
##
##GraphWarning3.Draw("AC*")
##outFile.cd()
#GraphWarning3.Write()
#
## row 11 col 30 TDAC 2 inj 0
#
#GraphWarning4 = TGraph()
#GraphWarning4.SetPoint(0,0.932,800)
#GraphWarning4.SetPoint(1,0.933,150)
#GraphWarning4.SetPoint(2,0.934,30)
#GraphWarning4.SetPoint(3,0.935,6)
#GraphWarning4.SetPoint(4,0.936,2)
#GraphWarning4.SetPoint(5,0.937,1)
#GraphWarning4.SetPoint(6,0.938,1)
#GraphWarning4.SetPoint(7,0.939,0)
#GraphWarning4.SetPoint(8,0.94,0)
#GraphWarning4.SetPoint(9,0.95,0)
#GraphWarning4.SetPoint(10,1,0)
#
#
##Xaxis = GraphWarning4.GetXaxis()
##Xaxis.SetLimits(0.,16.)
##GraphWarning4.GetHistogram().SetMaximum(2000.)
##GraphWarning4.GetHistogram().SetMinimum(0.)
##
##GraphWarning4.Draw("AC*")
##outFile.cd()
#GraphWarning4.Write()
#
## row 11 col 30 TDAC 7 inj 0
#
#GraphWarning5 = TGraph()
#GraphWarning5.SetPoint(0,0.896,2600)
#GraphWarning5.SetPoint(1,0.897,800)
#GraphWarning5.SetPoint(2,0.898,120)
#GraphWarning5.SetPoint(3,0.899,30)
#GraphWarning5.SetPoint(4,0.9,5)
#GraphWarning5.SetPoint(5,0.901,2)
#GraphWarning5.SetPoint(6,0.902,1)
#GraphWarning5.SetPoint(7,0.905,0)
#GraphWarning5.SetPoint(8,0.91,0)
#GraphWarning5.SetPoint(9,0.95,0)
#
#
##Xaxis = GraphWarning5.GetXaxis()
##Xaxis.SetLimits(0.,16.)
##GraphWarning5.GetHistogram().SetMaximum(2000.)
##GraphWarning5.GetHistogram().SetMinimum(0.)
##
##GraphWarning5.Draw("AC*")
##outFile.cd()
#GraphWarning5.Write()
#
#
## row 11 col 30 TDAC 14 inj 0
#
#GraphWarning6 = TGraph()
#GraphWarning6.SetPoint(0,0.833,2000)
#GraphWarning6.SetPoint(1,0.834,546)
#GraphWarning6.SetPoint(2,0.835,100)
#GraphWarning6.SetPoint(3,0.836,20)
#GraphWarning6.SetPoint(4,0.837,2)
#GraphWarning6.SetPoint(5,0.838,1)
#GraphWarning6.SetPoint(6,0.839,0)
#GraphWarning6.SetPoint(7,0.84,0)
#GraphWarning6.SetPoint(8,0.85,0)
#
##Xaxis = GraphWarning6.GetXaxis()
##Xaxis.SetLimits(0.,16.)
##GraphWarning6.GetHistogram().SetMaximum(2000.)
##GraphWarning6.GetHistogram().SetMinimum(0.)
##
##GraphWarning6.Draw("AC*")
##outFile.cd()
#GraphWarning6.Write()
#
#
## ---- Customize TGraph
#
#
#GraphWarning.SetLineWidth(2);
#GraphWarning.SetLineColor(2);
#GraphWarning.SetMarkerColor(2) # 9 ou 8
#GraphWarning.SetMarkerSize(0.7);
#GraphWarning.SetMarkerStyle(21); # 22 ou 33
#GraphWarning.SetTitle("Pixel row 11 column 30");
#GraphWarning.GetXaxis().SetTitle("global threshold [V]");
#GraphWarning.GetYaxis().SetTitle("probe (128 injections)");
#
#GraphWarning2.SetLineWidth(2);
#GraphWarning2.SetLineColor(9);
#GraphWarning2.SetMarkerColor(9) # 9 ou 8
#GraphWarning2.SetMarkerSize(0.8);
#GraphWarning2.SetMarkerStyle(22); # 22 ou 33
#GraphWarning2.SetTitle("Pixel row 11 column 30");
#GraphWarning2.GetXaxis().SetTitle("global threshold [V]");
#GraphWarning2.GetYaxis().SetTitle("probe (128 injections)");
#
#GraphWarning3.SetLineWidth(2);
#GraphWarning3.SetLineColor(8);
#GraphWarning3.SetMarkerColor(8) # 9 ou 8
#GraphWarning3.SetMarkerSize(0.8);
#GraphWarning3.SetMarkerStyle(23); # 22 ou 33
#GraphWarning3.SetTitle("Pixel row 11 column 30");
#GraphWarning3.GetXaxis().SetTitle("global threshold [V]");
#GraphWarning3.GetYaxis().SetTitle("probe (128 injections)");
#
#GraphWarning4.SetLineWidth(2);
#GraphWarning4.SetLineColor(8);
#GraphWarning4.SetMarkerColor(8) # 9 ou 8
#GraphWarning4.SetMarkerSize(0.8);
#GraphWarning4.SetMarkerStyle(23); # 22 ou 33
#GraphWarning4.SetTitle("Pixel row 11 column 30");
#GraphWarning4.GetXaxis().SetTitle("global threshold [V]");
#GraphWarning4.GetYaxis().SetTitle("probe (128 injections)");
#
#GraphWarning5.SetLineWidth(2);
#GraphWarning5.SetLineColor(2);
#GraphWarning5.SetMarkerColor(2) # 9 ou 8
#GraphWarning5.SetMarkerSize(0.8);
#GraphWarning5.SetMarkerStyle(21); # 22 ou 33
#GraphWarning5.SetTitle("Pixel row 11 column 30");
#GraphWarning5.GetXaxis().SetTitle("global threshold [V]");
#GraphWarning5.GetYaxis().SetTitle("probe (128 injections)");
#
#GraphWarning6.SetLineWidth(2);
#GraphWarning6.SetLineColor(9);
#GraphWarning6.SetMarkerColor(9) # 9 ou 8
#GraphWarning6.SetMarkerSize(0.8);
#GraphWarning6.SetMarkerStyle(22); # 22 ou 33
#GraphWarning6.SetTitle("Pixel row 11 column 30");
#GraphWarning6.GetXaxis().SetTitle("global threshold [V]");
#GraphWarning6.GetYaxis().SetTitle("probe (128 injections)");
#
## -- Canvas warning pixels
#CanvGraph1 = ROOT.TCanvas("Graph","Graph",400,400)
##CanvGraph1.cd()
#
#
#gStyle.SetOptStat()
##gStyle.SetStatX(0.9)
##gStyle.SetStatY(0.95)
#
##points6Warning2D.GetZaxis().SetTitleOffset(1.3)
##gPad.SetRightMargin(0.15)
#
##points6Warning2D.Draw("colz")
##list_TLine2=[]
##for i in range(0,25):
##	line_vert =  TLine(i,12,i,48)
##	line_vert.Draw()
##	list_TLine2.append(line_vert)
##
##for i in range(12,49):
##	line_hor =  TLine(0,i,24,i)
##	line_hor.Draw()
##	list_TLine2.append(line_hor)
#	
#GraphWarning.Draw("ALP")
#GraphWarning2.Draw("LPsame")
#GraphWarning3.Draw("LPsame")
#GraphWarning4.Draw("LPsame")
#GraphWarning5.Draw("LPsame")
#GraphWarning6.Draw("LPsame")
#
#leg = TLegend(0.9,0.7,0.7,0.9);
#leg.SetHeader("TDAC value");
#leg.AddEntry(GraphWarning3,"TDAC = 2","lp");
#leg.AddEntry(GraphWarning,"TDAC = 7","lp");
#leg.AddEntry(GraphWarning2,"TDAC = 14","lp");
##leg.AddEntry(GraphWarning4,"TDAC = 2","lp");
##leg.AddEntry(GraphWarning5,"TDAC = 7","lp");
##leg.AddEntry(GraphWarning6,"TDAC = 14","lp");
#leg.Draw();
#	
#	
#
#gPad.Update()
#
#
#CanvGraph1.Write()
#
#
#
#
#
## ---- Graph temperature VS threshold
#
#
#TempVSthresh = TGraph()
#TempVSthresh.SetPoint(0,20,735)
#TempVSthresh.SetPoint(1,0,641)
#TempVSthresh.SetPoint(2,-10,637)
#TempVSthresh.SetPoint(3,-20,673)
#
#
#
#Xaxis = TempVSthresh.GetXaxis()
#Xaxis.SetLimits(-25,25)
#TempVSthresh.GetHistogram().SetMaximum(800.)
#TempVSthresh.GetHistogram().SetMinimum(0.)
#
#TempVSthresh.SetLineWidth(1);
#TempVSthresh.SetLineColor(2);
##TempVSthresh.SetMarkerColor(2) # 9 ou 8
#TempVSthresh.SetMarkerSize(1.2);
#TempVSthresh.SetMarkerStyle(21); # 22 ou 33
#TempVSthresh.SetTitle("Threshold mean VS temperature");
#TempVSthresh.GetXaxis().SetTitle("Temperature");
#TempVSthresh.GetYaxis().SetTitle("Threshold distribution mean");
#
#outFile.cd()
#TempVSthresh.Write()
#
#CanvTempVSthresh = TCanvas("TempVSthresh","TempVSthresh",400,400)
#gStyle.SetOptStat()
#
#TempVSthresh.Draw("A*")
##TempVSthresh.Draw("ALP")
#	
#	
#
#gPad.Update()
#
#
#CanvTempVSthresh.Write()
#
#
#
#
#
##
### Write TDACfile.txt (must be at the end of the code) 
##
##cnt=0
##for i in file_TDAC_list:
##	
##	if cnt <1439:
##		file_TDAC.write(""+str(file_TDAC_list[cnt])+"\r\n")    # \r in order to cope windows
##	else:                                                           #necessary to avoid the last blank line in the output file
##		file_TDAC.write(str(file_TDAC_list[cnt]))              #check if this is necessary for the software ---> it is not TODO: remove	
##	cnt += 1
##file_TDAC.close()
##
#
#
##------------------------------ notes
#
##other
##execfile("~/Documents/CERN\ master\ thesis/python\ scripts/ThresholdScan/CCPDv2/t.pyt.py")
##os.system("root -l") # +str(sys.argv[2])+"")
#
##os.system("2+2")
#
#
##execfile("t.py")
