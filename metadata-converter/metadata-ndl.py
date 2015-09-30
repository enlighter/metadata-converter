
# main NDL metadata structure:
ndl_mt = {
	### Generic metadata ###
	'contributor' : {
		'author' : [],
		'illustrator' : [],
		'editor' : [],
		'default' : []
	},
	'coverage' : {
		'temporal' : [],
		'spatial' : [],
		'default' : [],
	},
	'creator' : [],
	'date' : {
		'created' : [],
		'issued' : [],
		'modified' : [],
		'valid' :[],
		'copyright' : [],
		'default' :[],
	},
	'description' : {
		'toc' : [], #table of contents
		'abstract' : [],
		'default' : [],
	},
	'format' : {
		'extent' : [],
		'medium' : [],
		'mimetype' : [],
		'default' : [],
	},
	'identifier' : {
		'isbn' : [],
		'issn' : [],
		'uri' : [],
		'citation' : [], #bibliographic citations
		'default' : [],
	},
	'language' : [],
	'publisher' : [],
	'relation' : {
		'isreferencedby' : [],
		'ispartof' : [],
		'requires' : [],
		'hasformat' : [],
		'haspart' : [],
		'isformatof' : [],
		'isreplacedby' : [],
		'isversionof' : [],
		'references' : [],
		'replaces' : [],
	},
	'rights' : [],
	'source' : [],
	'subject' : [],
	'title' : {
		'alttitle' : [], #alternative title
		'default' : [],
	},

	### Educational metadata ###
	'education' : {
		'eductionalalignment' : [],
		'eductionalalignmentboard' : [],
		'typeoflearningmaterial' :[],
		'eductionalalignmentprereq' : [], #educationalAlignment [Prerequisitetopic]
		'alignmenttype' : [],
		'educationalrole' : [],
		'educationaluse' : [],
		'interacttype' : [], #interactivityType
		'learntime' : [], #typicalLearningTime
		'accessibility' : [], #Accessibility related fields
	},

	### Multimedia Metadata (MPEG7) ###
	'multimedia' : [],

	### Theses & Dissertation Metadata ###
	'theses' : {
		'advisor' : [],
		'dateawarded' : [],
		'keyword' : [],
		'place' : [],
		'publisherdepartment' : [],
		'publisherinstitution' : [],
		'researcher' : [],
		'typedegree' : [],
	},
};