/*
A KBase module: compare_models_multiple
This sample module contains one small method - count_contigs.
*/

module compare_models_multiple {
	/*
	A string representing a ModelSet id.
	*/
	typedef string modelSet_id;
	
	/*
	A string representing a workspace name.
	*/
	typedef string workspace_name;
	
	typedef structure {
		string model_id;
		list <string> pegIDs;
	} ModelPegs;

	typedef structure {
	    	int core;
		int nonCore;
		string equation;
		string role;
		string ss;
		string class;
		string subClass;
		int numOfModels;
		float fractionModels;
		list <ModelPegs> pegs;
	} ReactionInfo;
	
	/*
	Comparative analysis of multiple models
	
	*/
	funcdef count_contigs(workspace_name,modelSet_id) returns (ReactionInfo) authentication required;
};
