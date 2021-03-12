% Generation of retrocue trials

% Creating 64 uniques trials
% 4 attended category-types
% 4 unattended category-types
% 2 cues (remember 1 or remember 2)
% 2 
% SINGLE load condition - 2 items in at. and 2 in unat.

numTrials = 64;
numTrialsRun = 16;
catTypes = [{'FM'}, {'FF'}, {'SO'}, {'SI'}];
cue = [1,2,1,2];
congruentAtt = [1 0];
buttonPressAtt = [{'right'},{'left'},{'left'},{'right'}]; %How do we want to control button preses; switch on each run?
arrow = [{'>'},{'<'},{'>'},{'<'}];
rightLeftImageProbe = [1 2];

attended = repelem(catTypes, length(catTypes))';
unattended = repmat(catTypes,[1,length(catTypes)])';
attended = repmat(attended,[numTrials/length(attended),1]); 
unattended = repmat(unattended,[numTrials/length(unattended),1]);

cue = repelem(cue, numTrials/length(cue))';
congruentAtt = repelem(congruentAtt, numTrials/length(congruentAtt))'; 

buttonPressAtt_full = repelem(buttonPressAtt,1,numTrials/(length(buttonPressAtt)))'; %repmat({'None'},1,numTrials/2)']; 
arrow_full = repelem(arrow,1,numTrials/length(arrow))';

full = [attended,unattended,num2cell(cue),num2cell(congruentAtt),buttonPressAtt_full,arrow_full];

trialMix = randperm(numTrialsRun);
trialMixFull = [];
for m = 1:numTrials/numTrialsRun
    trialMixFull = [trialMixFull,{trialMix(m:numTrials/numTrialsRun:end)}];
end

% MAKE THIS NOT HARD-CODED
trialMixFull = [trialMixFull; trialMixFull([2 1 4 3]);trialMixFull([3 4 1 2]);trialMixFull([4 3 2 1])];

full_runs = cell(numTrialsRun*numTrials/numTrialsRun,size(full,2));
for run = 1:size(trialMixFull,1)
    for part = 1:size(trialMixFull,2)
        full_runs(((run-1)*numTrialsRun)+(part-1)*4+1:((run-1)*numTrialsRun)+(part-1)*4+4,1:6) = full([numTrialsRun*(part-1)+trialMixFull{run,part}],:); 
    end
end

full_runs = [full_runs, num2cell(repelem(1:numTrials/numTrialsRun,numTrialsRun)')];

images_fm = dir(fullfile(pwd,'images','*fm.jpg'));
images_ff = dir(fullfile(pwd,'images','*ff.jpg'));
images_si = dir(fullfile(pwd,'images','*si.jpg'));
images_so = dir(fullfile(pwd,'images','*so.jpg'));

nOrigImages = 21; 
% we have 20 unique trials where a category-type will be used
% each trial will have 2 images of this category type - we need 80 unique
% images or 20 images where each image repeats four times across all four runs. 
% an extra 1 per run comes for the non-match uncued memory probe 

fm_IDs=[];
ff_IDs=[];
si_IDs=[];
so_IDs=[];
for rr = 1:numTrials/numTrialsRun
    fm_IDs = [fm_IDs,randperm(length(images_fm),nOrigImages)];
    ff_IDs = [ff_IDs,randperm(length(images_ff),nOrigImages)];
    si_IDs = [si_IDs,randperm(length(images_si),nOrigImages)];
    so_IDs = [so_IDs,randperm(length(images_so),nOrigImages)];
end

fm_unc = fm_IDs(nOrigImages:nOrigImages:end);
ff_unc = ff_IDs(nOrigImages:nOrigImages:end);
si_unc = si_IDs(nOrigImages:nOrigImages:end);
so_unc = so_IDs(nOrigImages:nOrigImages:end);

fm_unc = {images_fm(fm_unc).name};
fm_unc = strcat('images/',fm_unc);
ff_unc = {images_ff(ff_unc).name};
ff_unc = strcat('images/',ff_unc);
so_unc = {images_so(so_unc).name};
so_unc = strcat('images/',so_unc);
si_unc = {images_si(si_unc).name};
si_unc = strcat('images/',si_unc);


uncProbeImages = [fm_unc;ff_unc;so_unc;si_unc];

fm_IDs(nOrigImages:nOrigImages:end) = [];
ff_IDs(nOrigImages:nOrigImages:end) = [];
si_IDs(nOrigImages:nOrigImages:end) = [];
so_IDs(nOrigImages:nOrigImages:end) = [];

fm_IDs = {images_fm(fm_IDs).name};
fm_sc = Shuffle(strcat('scrambles/',fm_IDs));
fm_IDs = strcat('images/',fm_IDs);

ff_IDs = {images_ff(ff_IDs).name};
ff_sc = Shuffle(strcat('scrambles/',ff_IDs));
ff_IDs = strcat('images/',ff_IDs);

si_IDs = {images_si(si_IDs).name};
si_sc = Shuffle(strcat('scrambles/',si_IDs));
si_IDs = strcat('images/',si_IDs);

so_IDs = {images_so(so_IDs).name};
so_sc = Shuffle(strcat('scrambles/',so_IDs));
so_IDs = strcat('images/',so_IDs);

images_full = [fm_IDs',ff_IDs',so_IDs',si_IDs'];
scrambles_full = [fm_sc',ff_sc',so_sc',si_sc'];
probeSelect = Shuffle(repmat(rightLeftImageProbe,length(buttonPressAtt_full)/(2*length(catTypes)*length(rightLeftImageProbe)),size(catTypes,2))');

% Add five images 
imagesAdded = cell(numTrialsRun*numTrials/numTrialsRun,9); 
countTy = [1,1,1,1];
countSc = [1,1,1,1];
countProbe = [1,1,1,1];
for run2 = 1:numTrials/numTrialsRun
    for trial = 1:numTrialsRun
        for ty = 1:length(catTypes)
            if strcmp(full_runs{(run2-1)*numTrialsRun+trial,1},catTypes{ty}) && full_runs{(run2-1)*numTrialsRun+trial,3}==1
                imagesAdded((run2-1)*numTrialsRun+trial,1) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                imagesAdded((run2-1)*numTrialsRun+trial,2) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                
                imagesAdded((run2-1)*numTrialsRun+trial,6) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;                
                imagesAdded((run2-1)*numTrialsRun+trial,7) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;     
                
                if full_runs{(run2-1)*numTrialsRun+trial,4}==1
                    pictureSelect = imagesAdded((run2-1)*numTrialsRun+trial,1:2);
                    imagesAdded((run2-1)*numTrialsRun+trial,5) = pictureSelect(probeSelect(countProbe(ty),ty));
                    countProbe(ty)=countProbe(ty)+1;
                elseif full_runs{(run2-1)*numTrialsRun+trial,4}==0
                    imagesAdded((run2-1)*numTrialsRun+trial,5) = images_full(countTy(ty),ty);
                    countTy(ty)=countTy(ty)+1;
                end                   
            end  
            
            if strcmp(full_runs{(run2-1)*numTrialsRun+trial,2},catTypes{ty}) && full_runs{(run2-1)*numTrialsRun+trial,3}==1
                imagesAdded((run2-1)*numTrialsRun+trial,3) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                imagesAdded((run2-1)*numTrialsRun+trial,4) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                
                imagesAdded((run2-1)*numTrialsRun+trial,8) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;                
                imagesAdded((run2-1)*numTrialsRun+trial,9) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;                
            end 
                
            if strcmp(full_runs{(run2-1)*numTrialsRun+trial,1},catTypes{ty}) && full_runs{(run2-1)*numTrialsRun+trial,3}==2
                imagesAdded((run2-1)*numTrialsRun+trial,3) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                imagesAdded((run2-1)*numTrialsRun+trial,4) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                
                imagesAdded((run2-1)*numTrialsRun+trial,8) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;                
                imagesAdded((run2-1)*numTrialsRun+trial,9) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;
                
                if full_runs{(run2-1)*numTrialsRun+trial,4}==1
                    pictureSelect = imagesAdded((run2-1)*numTrialsRun+trial,3:4);
                    imagesAdded((run2-1)*numTrialsRun+trial,5) = pictureSelect(probeSelect(countProbe(ty),ty));
                    countProbe(ty)=countProbe(ty)+1;
                elseif full_runs{(run2-1)*numTrialsRun+trial,4}==0
                    imagesAdded((run2-1)*numTrialsRun+trial,5) = images_full(countTy(ty),ty);
                    countTy(ty)=countTy(ty)+1;
                end
            end                 
                
            if strcmp(full_runs{(run2-1)*numTrialsRun+trial,2},catTypes{ty}) && full_runs{(run2-1)*numTrialsRun+trial,3}==2
                imagesAdded((run2-1)*numTrialsRun+trial,1) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                imagesAdded((run2-1)*numTrialsRun+trial,2) = images_full(countTy(ty),ty);
                countTy(ty)=countTy(ty)+1;
                
                imagesAdded((run2-1)*numTrialsRun+trial,6) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;                
                imagesAdded((run2-1)*numTrialsRun+trial,7) = scrambles_full(countSc(ty),ty);
                countSc(ty)=countSc(ty)+1;                
            end                      
        end
    end
end

full_runs = [imagesAdded,full_runs];
full_runs = cell2table(full_runs); 
full_runs.Properties.VariableNames = {'image1L','image1R','image2L','image2R','imageCuedProbe','scramble1L','scramble1R','scramble2L','scramble2R','cuedType','uncuedType','cue','probeCorrect','buttonCorrect','arrow','run'};


numUncueTrials = numTrialsRun/4; %1/4 of trials probe uncued memory

% Things controlled for within a run

uncuedParams = Shuffle(repmat([repmat(rightLeftImageProbe',numTrials/(4*length(catTypes)*length(rightLeftImageProbe)),1),repmat([1;0],numTrials/(4*length(catTypes)*length([1 0])),1)],1,1,4)); 
% [count, item, categoty-type] - count = how many time c-t has already
% occured
% item - control for both match/non-match and right/left image from uncued memory set

uncuedTable = cell(numTrialsRun*numTrials/numTrialsRun,3); 


for run3 = 1:numTrials/numTrialsRun
    while 1
        uncueCat = [catTypes(randperm(length(catTypes)));repmat([{1},{2}],1,numUncueTrials/2)];
        uncueButtonLocation = [(repmat([{'right'},{'left'},{'left'},{'right'}],1,numUncueTrials/4));(repmat([{1},{0}],1,numUncueTrials/2))];
        uncueButtonLocation = uncueButtonLocation(:,randperm(length(uncueButtonLocation)));       
        uncueTrials = [uncueCat; uncueButtonLocation];
        
        uncuedTableRun = cell(numTrialsRun,3); 
        plus=0;
        uncuedCount = [1 1 1 1];

        for trialUnc = 1:numTrialsRun/4
            prez = strcmp(full_runs.uncuedType,uncueTrials(1,trialUnc)) & full_runs.cue==uncueTrials{2,trialUnc} & full_runs.probeCorrect==uncueTrials{4,trialUnc} & strcmp(full_runs.buttonCorrect,uncueTrials(3,trialUnc)) & full_runs.run==run3 & ~strcmp(full_runs.cuedType,uncueTrials(1,trialUnc));
            if sum(prez)>=1
                plus = plus+1;
                if uncueTrials{2,trialUnc}==1

                    if uncuedParams(uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)),2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))==1
                        uncueWhichCount = uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)); %select which category-type 
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),2) = {uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))};                       
                        uncueImageSelect = imagesAdded(find(prez,1,'first'),3:4); %select the two images 
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),1) = uncueImageSelect(uncuedParams(uncueWhichCount,1,find(strcmp(catTypes,uncueTrials(1,trialUnc)))));
                    
                    elseif uncuedParams(uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)),2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))==0
                        uncueWhichCount = uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)); %select which category-type 
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),2) = {uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))};                                              
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),1)=uncProbeImages(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1),run3);
                    end
                                        
                    % This section selects the correct response for the
                    % uncued item
                    if uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc)))) ==0
                        if strcmp(full_runs.arrow(find(prez,1,'first')),arrow(1))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(3);
                        elseif strcmp(full_runs.arrow(find(prez,1,'first')),arrow(2))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(4);
                        end
                    elseif uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc)))) ==1
                        if strcmp(full_runs.arrow(find(prez,1,'first')),arrow(1))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(1);
                        elseif strcmp(full_runs.arrow(find(prez,1,'first')),arrow(2))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(2);
                        end                            
                    end                       
                        
                    uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1))= uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1))+1;
               
                elseif uncueTrials{2,trialUnc}==2
                    if uncuedParams(uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)),2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))==1
                        uncueWhichCount = uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)); %select which category-type 
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),2) = {uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))};                       
                        uncueImageSelect = imagesAdded(find(prez,1,'first'),1:2); %select the two images 
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),1) = uncueImageSelect(uncuedParams(uncueWhichCount,1,find(strcmp(catTypes,uncueTrials(1,trialUnc)))));
                    
                    elseif uncuedParams(uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)),2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))==0
                        uncueWhichCount = uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1)); %select which category-type 
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),2) = {uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc))))};                                              
                        uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),1)=uncProbeImages(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1),run3);
                    end
                    
                    % This section selects the correct response for the
                    % uncued item
                    if uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc)))) ==0
                        if strcmp(full_runs.arrow(find(prez,1,'first')),arrow(1))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(3);
                        elseif strcmp(full_runs.arrow(find(prez,1,'first')),arrow(2))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(4);
                        end
                    elseif uncuedParams(uncueWhichCount,2,find(strcmp(catTypes,uncueTrials(1,trialUnc)))) ==1
                        if strcmp(full_runs.arrow(find(prez,1,'first')),arrow(1))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(1);
                        elseif strcmp(full_runs.arrow(find(prez,1,'first')),arrow(2))
                            uncuedTableRun(find(prez,1,'first')-((run3-1)*numTrialsRun),3) = buttonPressAtt(2);
                        end                            
                    end                       
                        
                    uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1))= uncuedCount(find(strcmp(catTypes,uncueTrials(1,trialUnc)),1))+1;
                end                
    
            end
        end
        if plus==4
            uncuedTable((run3-1)*numTrialsRun+1:run3*numTrialsRun,:) = uncuedTableRun; 
            break
        end
    end
end        

uncuedProbePrez = [];

for uncuePrez = 1:numTrials
    if isempty(uncuedTable{uncuePrez,1})
        uncuedProbePrez = [uncuedProbePrez;{0}];
    elseif ~isempty(uncuedTable{uncuePrez,1})
        uncuedProbePrez = [uncuedProbePrez;{1}];
    end
end
        
uncuedTable(find(cellfun(@isempty,uncuedTable(:,1)))) = {'none'};

uncuedTable = [uncuedTable,uncuedProbePrez];

uncuedTable = cell2table(uncuedTable); 
uncuedTable.Properties.VariableNames = {'imageUncuedProbe','uncuedProbeCorrect','uncuedButtonCorrect','probeNonCued'};


full_runs = [full_runs,uncuedTable];

for run_final = 1:numTrials/numTrialsRun
    run_perm = full_runs(full_runs.run==run_final,:);
    run_perm = run_perm(randperm(size(run_perm,1)),:);
    full_runs(full_runs.run==run_final,:) = run_perm;
    writetable(run_perm,['trials_',num2str(run_final),'.csv']);
    save(['trials_',num2str(run_final),'.mat'],'run_perm');
end
    

writetable(full_runs,'fullTrials.csv');
save('fullTrials.mat','full_runs');


