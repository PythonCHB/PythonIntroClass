
SZ_TYPE =        0x00
DWORD_TYPE =     0x01
BOOL_TYPE =      0x02
MULTI_SZ_TYPE =  0x03
ENUM_TYPE =      0x04
FILE_TYPE =      0x05

dic = {
	SZ_TYPE : "LWC_SZ",
	DWORD_TYPE : "LWC_DWORD" ,
	BOOL_TYPE : "LWC_BOOL",
	MULTI_SZ_TYPE : "LWC_MULTI_SZ",
	ENUM_TYPE : "",
	FILE_TYPE : "LWC_SZ",
	}

typeDic = {
	SZ_TYPE : "<string>",
	DWORD_TYPE : "<int>" ,
	BOOL_TYPE : "<boolean>",
	MULTI_SZ_TYPE : "[ <string>, ...]",
	ENUM_TYPE : "<string>",
	FILE_TYPE : "<path>",
	}

schemaDic = {
	SZ_TYPE : "STRING",
	DWORD_TYPE : "INTEGER" ,
	BOOL_TYPE : "BOOLEAN",
	MULTI_SZ_TYPE : "ARRAY(`STRING')",
	ENUM_TYPE : "STRING",
	FILE_TYPE : "STRING",
	}

REGPATH_LSASS =         "registry.Services.lsass"
REGPATH_PARAMETERS =    "registry.Services.lsass.Parameters"
REGPATH_ZONES =         "registry.Services.lsass.Parameters.Zones"
REGPATH_PROVIDERS =     "registry.Services.lsass.Parameters.Providers"
REGPATH_AD =            "registry.Services.lsass.Parameters.Providers.ActiveDirectory"
REGPATH_FILE =          "registry.Services.lsass.Parameters.Providers.File"
REGPATH_FILE_INSTANCE = "registry.Services.lsass.Parameters.Providers.File.Instance"
REGPATH_LOCAL =         "registry.Services.lsass.Parameters.Providers.Local.Instance.System"
REGPATH_NSS =           "registry.Services.lsass.Parameters.Providers.Nss"
REGPATH_NTLM =          "registry.Services.lsass.Parameters.NTLM"
REGPATH_AUTH =          "services.auth"
REGPATH_LDAP =          "registry.Services.lsass.Parameters.Providers.Ldap"
REGPATH_LDAP_INSTANCE = "registry.Services.lsass.Parameters.Providers.Ldap.Instance"
REGPATH_NIS =           "registry.Services.lsass.Parameters.Providers.Nis"
REGPATH_NIS_INSTANCE =  "registry.Services.lsass.Parameters.Providers.Nis.Instance"
KEYPREFIX_LDAP_RFC2307 ="rfc2307_"
KEYPREFIX_LDAP_AD =     "ad_"
KEYPREFIX_LDAP_LDAPSAM ="ldapsam_"

CONFIG_CLASS_LDAP = ""
CONFIG_CLASS_LDAP_ATTRIB =""
CONFIG_CLASS_LDAP = ""
CONFIG_CLASS_LSASS = ""
CONFIG_CLASS_KIDMAP = ""
CONFIG_CLASS_KIDMAP = ""
CONFIG_CLASS_ID = ""
CONFIG_CLASS_AUTH = ""
CONFIG_CLASS_LOCAL = ""
CONFIG_CLASS_AD = ""
CONFIG_CLASS_NIS = ""
CONFIG_CLASS_FILE = ""


instance = ""
SystemZone = True

class LWRegSysctlStringValidator():
	def __init__(self, sysctl, default, valid=None):
		self.sysctl = sysctl
		self.default = default
		self.valid = valid

class ZoneIdValidator():
	def __init__(self, path, key, subkey=None, instance=None):
		self.path = path
		self.key = key
		self.subkey = subkey
		self.instance = instance

class LWRegSysctlLongValidator():
	def __init__(self, sysctl, default, read_only=False):
		self.sysctl = sysctl
		self.default = default
		self.read_only = read_only
		
class LWRegSysctlStore():
	def __init__(self, sysctl, default, read_only=False):
		self.sysctl = sysctl
		self.default = default
		self.read_only = read_only
		
class IdmapValidator():
	def __init__(self, user_range, default):
		self.user_range = user_range
		self.default = default
		
class AuthRulesValidator():
	def __init__(self, path, key, subkey=None, instance=None):
		self.path = path
		self.key = key
		self.subkey = subkey
		self.instance = instance
		
class LWRegGconfMultiStringValidator():
	def __init__(self, path, key, valid=None, subkey=None, instance=None,range=None):
		self.path = path
		self.key = key
		self.valid = valid
		self.subkey = subkey
		self.instance = instance
		self.range = range
		
class LWRegGconfLdapServerMultiStringValidator():
	def __init__(self, path, key, valid=None, subkey=None, instance=None,range=None):
		self.path = path
		self.key = key
		self.valid = valid
		self.subkey = subkey
		self.instance = instance
		self.range = range

class LWRegGconfStringValidator():
	def __init__(self, path, key, valid=None, subkey=None, instance=None, read_only=False):
		self.path = path
		self.key = key
		self.valid = valid
		self.subkey = subkey
		self.instance = instance
		self.read_only = read_only

class LWRegGconfLongValidator():
	def __init__(self, path, key, range=None, valid=None, subkey=None, instance=None, read_only=False):
		self.path = path
		self.key = key
		self.range = range
		self.valid = valid
		self.subkey = subkey
		self.instance = instance
		self.read_only = read_only
		

class LWRegGconfBooleanValidator():
	def __init__(self, path, key, valid=None, subkey=None, instance=None, read_only=False):
		self.path = path
		self.key = key
		self.valid = valid
		self.subkey = subkey
		self.instance = instance
		self.read_only = read_only
		
class LWRegGconfFileValidator():
	def __init__(self, path, key, valid=None, subkey=None, instance=None, range=None):
		self.path = path
		self.key = key
		self.valid = valid
		self.subkey = subkey
		self.instance = instance
		self.range = range

class WorkgroupValidator(LWRegGconfStringValidator):
	def __init__(self, path, key):
		self.path = path
		self.key = key
		
class LocalSamDbNameValidator():
	def __init__(self, path, key):
		self.path = path
		self.key = key

class NisHostnameLookupValidator():
	def __init__(self):
		print ""

libGlobal =[{
            "name": "lsass-log-level",
            "description": "Default log level for lsassd on startup. "
                            "Acceptable values range from 0 to 7.",
            "doc": "This setting sets the default logging level for lsassd "
                   "across the cluster.  Starting at 0, successive levels "
                   "provide more information.  The most detailed information "
                   "is available at level 7.  These logs are designed "
                   "to be read and interpreted by Isilon Support.  "
                   "This setting only takes effect after a service restart.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LSASS,
                key="DefaultLogLevel", range=(0, 7)),
        }, {
            "name": "send-ntlmv2",
            "description": "Send NTLMv2 responses",
            "doc": "When connecting as a SMB client, this setting configures "
                   "the type of NTLM response we send.  NTLMv2 provides additional "
                   "security over NTLM and should be used if all servers support "
                   "the protocol.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NTLM,
                key="SendNTLMv2"),
        }, {
            "name": "load-providers",
            "description": "The ordered list of providers to be loaded by lsassd.",
            "doc": "This list controls which providers will be loaded by lsassd "
                   "and what order they will be loaded in.  Please use the "
                   "provider-list setting if you wish to change the "
                   "resolution order.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_PROVIDERS,
                key="LoadOrder", valid=["ActiveDirectory","Local","Nss","File","Ldap","Nis"]),
            "hidden": True,
        }, {
            "name": "space-replacement",
            "description": "Space replacement",
            "doc": "Some clients have trouble when spaces appear within user "
                   "and group names.  This setting causes lsassd to substitute a "
                   "character whenever a space is encountered.  Care should be "
                   "taken when choosing a character so it doesn't conflict with "
                   "characters already used by the name.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_PARAMETERS,
                key="SpaceReplacement"),
        }, {
            "name": "mapper",
            "description": "Location of mapper module",
            "doc": "OneFS supports an extensible mapping infrastructure.  This "
                   "setting controls which mapping module is used.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_PARAMETERS,
                key="MapModulePath", subkey='Zones', instance="System"),
            "hidden": True
        }, {
            "name": "mapping-rules",
            "description": "Current ID Mapping rules",
            "cclass": CONFIG_CLASS_ID,
            "type": MULTI_SZ_TYPE,
            "validator": AuthRulesValidator(path=REGPATH_PARAMETERS,
                subkey="Zones", instance="System", key="MappingRules"),
        }, {
            "name": "provider-list",
            "description": "System Provider List",
            "cclass": CONFIG_CLASS_LSASS,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_PARAMETERS,
                subkey="Zones", instance="System", key="ProviderList"),
        }, {
            "name": "uid-range",
            "description": "Range of uids to use for allocating temporary uids",
            "doc": "When OneFS needs to allocate a UID, it will use the next unused "
                   "value from this range.  OneFS will not attempt to verify if "
                   "the uid is in use before allocation.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": SZ_TYPE,
            "validator": IdmapValidator(user_range=True, default=(1000000,2000000)),
            "hidden": False,
        } , {
            "name": "gid-range",
            "description": "Range of gids to use for allocating temporary gids",
            "doc": "When OneFS needs to allocate a GID, it will use the next unused "
                   "value from this range.  OneFS will not attempt to verify if "
                   "the GID is in use before allocation.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": SZ_TYPE,
            "validator": IdmapValidator(user_range=False, default=(1000000,2000000)),
            "hidden": False,
        }, {
            "name": "on-disk-identity",
            "description": "Preferred on-disk storage",
            "doc": "This setting controls what identity is stored on disk. "
                   "Valid options are native, unix and sid.  Note: If we're unable to "
                   "convert the identity to the preferred format, we will store it "
                   "on disk as-is. Modification of this setting only changes future "
                   "on-disk changes.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": SZ_TYPE,
            "validator": LWRegSysctlStringValidator(
                sysctl="efs.idmap.options.on_disk", default="native",
                valid=["native", "unix", "sid"])
        }, {
            "name": "min-mapped-rid",
            "description": "Starting rid in the local domain to map uids and gids",
            "doc": "Internal parameter to control unix users mapping onto "
                   "the local domain.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator":
                LWRegSysctlLongValidator(sysctl="efs.idmap.options.min_mapped_rid",
                    default=2147483648),
            "hidden": True,
        }, {
            "name": "alloc-retries",
            "description": "Number of times to retry an id allocation before failing",
            "doc":"",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator":
                LWRegSysctlLongValidator(sysctl="efs.idmap.options.alloc_retries",
                    default=5),
            "hidden": True,
        }, {
            "name": "system-uid-threshold",
            "description": "Minimum uid to attempt to look up in the idmap database",
            "doc": "As an optimization, OneFS assumes that UIDs under this value "
                   "will not have an explicit mapping to a SID.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator":
                LWRegSysctlLongValidator(
                    sysctl="efs.idmap.options.system_uid_threshold", default=80),
            "hidden": True,
        }, {
            "name": "system-gid-threshold",
            "description": "Minimum gid to attempt to lookup in the idmap database",
            "doc": "As an optimization, OneFS assumes that GIDs under this value "
                   "will not have an explicit mapping to a SID.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator":
                LWRegSysctlLongValidator(
                    sysctl="efs.idmap.options.system_gid_threshold", default=80),
            "hidden": True,
        }, {
            "name": "rpc-timeout",
            "description": "Maximum amount of time to wait (in seconds) for an idmap "
                "response.",
            "doc": "When making a request from the kernel to the idmapper, OneFS "
                   "will wait a fixed amount of time before processing the "
                   "response.  This setting controls the timeout.",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(
                sysctl="efs.idmap.options.rpc_timeout", default=30),
            "hidden": True,
        }, {
            "name": "rpc-max-requests",
            "description": "Maximum number of outstanding rpc requests",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(
                sysctl="efs.idmap.options.rpc_max_requests", default=16),
            "hidden": True,
        }, {
            "name": "rpc-block-time",
            "description": "Minimum amount of time to wait (in milliseconds) before "
                "performing an oprestart",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(
                sysctl="efs.idmap.options.rpc_block_time", default=5),
            "hidden": True,
        }, {
            "name": "cache-id-lifetime",
            "description": "Number of seconds to cache idmap id responses",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(
                sysctl="efs.idmap.options.id_lifetime", default=900),
            "hidden": True,
        }, {
            "name": "cache-cred-lifetime",
            "description": "Number of seconds to cache idmap cred responses",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(
                sysctl="efs.idmap.options.cred_lifetime", default=900),
            "hidden": True,
        }, {
            "name": "null-uid",
            "description": "UID to use when the kernel is unable to retrieve a uid "
                "for a persona.",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(sysctl="kern.null_uid",
                default=4294967293L),
            "hidden": True,
        }, {
            "name": "unknown-uid",
            "description": "UID to use for the unknown (anonymous) user",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(sysctl="kern.unknown_uid",
                default=4294967294L),
            "hidden": True,
        }, {
            "name": "group-uid",
            "description": "UID to use when the kernel needs to retrieve a uid for a "
                "group.",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(sysctl="kern.group_uid",
                default=4294967292L),
            "hidden": True,
        }, {
            "name": "null-gid",
            "description": "GID to use when the kernel is unable to retrieve a gid "
                "for a persona.",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(sysctl="kern.null_gid",
                default=4294967293L),
            "hidden": True,
        }, {
            "name": "unknown-gid",
            "description": "GID to use for the unknown (anonymous) group",
            "doc": "",
            "cclass": CONFIG_CLASS_KIDMAP,
            "type": DWORD_TYPE,
            "validator": LWRegSysctlLongValidator(sysctl="kern.null_gid",
                default=4294967294L),
            "hidden": True,
        }, {
            "name": "domain",
            "description": "Domain name used during join time.",
            "doc": "",
            "cclass": CONFIG_CLASS_AUTH,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AUTH,
                key="dns_domain"),
            "hidden": True,
        }, {
            "name": "workgroup",
            "description": "NetBIOS Workgroup/Domain",
            "doc": "",
            "cclass": CONFIG_CLASS_AUTH,
            "type": SZ_TYPE,
            "validator": WorkgroupValidator(path=REGPATH_AUTH,
                key="workgroup"),
        }, {
            "name": "join-dcname",
            "description": "Domain Controller used during join.",
            "doc": "",
            "cclass": CONFIG_CLASS_AUTH,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AUTH,
                key="join_dcname"),
            "hidden": True,
        }, {
            "name": "join-time",
            "description": "Domain join time",
            "doc": "",
            "cclass": CONFIG_CLASS_AUTH,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_AUTH,
                key="join_time"),
            "hidden": True,
        }, {
            "name": "last-zone-id",
            "description": "Last Zone Id allocated",
            "doc": "",
            "cclass": CONFIG_CLASS_LSASS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_PARAMETERS,
                key="LastZoneId", read_only=True),
            "hidden": True,
        }]#,{
       #     "name": "nis-hostname-lookup",
       #     "description": "Priority of NIS hostname lookups",
       #     "cclass": CONFIG_CLASS_AUTH,
       #     "type": SZ_TYPE,
       #     "validator": NisHostnameLookupValidator(),
       #     "hidden": False,
       # }

libZone  = [{
            "name": "map-untrusted",
            "description": "Map untrusted domains to this NetBIOS domain during "
                           "authentication.",
            "doc": "As part of the NTLMv1 and NTLMv2 protocols, a NetBIOS domain "
                   "is usually provided by the client computer, even if unspecified "
                   "by the operator.  This setting allows lsassd to map the unknown "
                   "domain into the one specified.  If no domain is specified, "
                   "the user is assumed to exist in the local domain.  Specifying "
                   "an Active Directory domain can cause issues with NTLMv2 "
                   "authentication",
            "cclass": CONFIG_CLASS_LSASS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_PARAMETERS,
                key="MapUntrusted", subkey='Zones', instance=instance),
        }, {
            "name": "zone-zone-id",
            "description": "Zone Id",
            "doc": "Zone Id for this Authentication Zone.  This value is "
                   "selected automatically and should not be adjusted.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": DWORD_TYPE,
            "validator": ZoneIdValidator(path=REGPATH_PARAMETERS,
                key="ZoneId", subkey='Zones', instance=instance),
        }, {
            "name": "system-provider",
            "description": "Minimum set of required users provided by this provider",
            "doc": "",
            "cclass": CONFIG_CLASS_LSASS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_PARAMETERS,
                key="SystemProvider", subkey='Zones', instance=instance,
                read_only=SystemZone),
            "hidden": True
        }, {
            "name": "alternate-system-provider",
            "description": "If system-provider isn't in the zone, use this",
            "doc": "",
            "cclass": CONFIG_CLASS_LSASS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_PARAMETERS,
                key="AltSystemProvider", subkey='Zones', instance=instance,
                read_only=SystemZone),
            "hidden": True
        }, {
            "name": "cache-size",
            "description": "Maximum size of in memory cache",
            "doc": "Each zone keeps an in-memory cache of frequently used "
                "objects.  Each object is approximately 1000 bytes.",
            "cclass": CONFIG_CLASS_LSASS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_PARAMETERS,
                key="MemoryCacheSizeCap", subkey='Zones', instance=instance,
                range=(1000000,50000000)),
        }, {
            "name": "user-mapping-rules",
            "description": "Current ID Mapping rules",
            "cclass": CONFIG_CLASS_ID,
            "type": MULTI_SZ_TYPE,
            "validator": AuthRulesValidator(path=REGPATH_PARAMETERS,
                subkey="Zones", instance=instance, key="MappingRules"),
        }, {
            "name": "auth-providers",
            "description": "List of providers",
            "cclass": CONFIG_CLASS_LSASS,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_PARAMETERS,
                subkey="Zones", instance=instance, key="ProviderList"),
        }, {
            "name": "smb-shares",
            "description": "List of shares",
            "cclass": CONFIG_CLASS_LSASS,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_PARAMETERS,
                subkey="Zones", instance=instance, key="ShareList"),
        }]

libLocal  = [{
            "name": "machine-name",
            "description": "Machine SamDB Name",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": SZ_TYPE,
            "validator": LocalSamDbNameValidator(path=REGPATH_LOCAL,
                key="SamDBName"),
        }, {
            "name": "min-password-age",
            "description": "Minimum password age for local accounts",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="MinPasswordAge"),
        }, {
            "name": "max-password-age",
            "description": "Maximum password age for local accounts",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="MaxPasswordAge"),
        }, {
            "name": "min-password-length",
            "description": "Minimum password length for local accounts",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="MinPasswordLength"),
        }, {
            "name": "password-prompt-time",
            "description": "Time remaining before prompting for local "
                "accounts password change",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="PasswordPromptTime"),
        }, {
            "name": "lockout-threshold",
            "description": "Number of incorrect password attempts "
                "before local account lockout.",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="LockoutThreshold"),
            "hidden": True,
        }, {
            "name": "lockout-duration",
            "description": "Length of time for local account lockout",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="LockoutDuration"),
            "hidden": True,
        }, {
            "name": "lockout-window",
            "description": "Window of time for local account lockout",
            "cclass": CONFIG_CLASS_LOCAL,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LOCAL,
                key="LockoutWindow"),
            "hidden": True,
        }]


libAd  = [{
            "name": "assume-default-domain",
            "description": "Lookup unqualified users in the primary trusted domain",
            "doc": "By default, Active Directory users must be referenced by either "
                   "their NT4 style name (DOMAIN\\user) or UPN (User Principal Name). "
                   "This setting controls the behavior of unqualified name lookup. "
                   "When this setting is enabled, unqualified names are looked up "
                   "as if they are prepended with the primary Active Directory "
                   "domain.  Additionally, names in the primary domain are returned "
                   "unqualified.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="AssumeDefaultDomain", subkey='Instance', instance=instance),
        }, {
            "name": "sfu-support",
            "description": "Services for Unix mode.  Valid values are: none, rfc2307",
            "doc": "Services For Unix (SFU) is an extension to the typical Active "
                   "Directory Schema.  When properly configured, information "
                   "normally required by unix clients (uid, home directory, shell, "
                   "etc) is stored along side the Windows accounts.  The most "
                   "common schema extension follows the attributes defined in "
                   "RFC 2307.  When this mode is enabled, those UNIX attributes "
                   "will be queried in addition to the normal set of Windows "
                   "attributes.  If these attributes do not exist, the defaults "
                   "are used.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="SFUSupport", valid=["none", "rfc2307"], subkey='Instance', instance=instance),
        }, {
            "name": "ad-cache-type",
            "description": "Active Directory cache type, Acceptable values: sqlite or memory",
            "doc": "Adjust the type of the Active Directory cache.  Unless you "
                   "encounter problems, the 'memory' cache is recommended.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="CacheType", valid=["sqlite", "memory"], subkey='Instance', instance=instance),
            "hidden": True
        }, {
            "name": "create-home-dir",
            "description": "Create Home Directory when AD users log in",
            "doc": "When logging in for the first time, a user's home directory "
                   "can be automatically created and provisioned.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="CreateHomeDir", subkey='Instance', instance=instance),
            "hidden": True
        }, {
            "name": "check-online-interval",
            "description": "Interval between domain online checks",
            "doc": "Lsassd tracks connectivity to domains in order to efficiently "
                   "handle retry and offline conditions without putting additional "
                   "stress on the network.  When a domain goes offline, this setting "
                   "controls the maximum amount of time we will wait before "
                   "attempting to contact the domain again.",
            "cclass": CONFIG_CLASS_AD,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_AD,
                key="DomainManagerCheckDomainOnlineInterval", range=(30, 3600),
                subkey='Instance', instance=instance),
        }, {
            "name": "home-dir-prefix",
            "description": "Home directory prefix",
            "doc": "When the unix home directory is not entered into Active "
                   "Directory, OneFS will generate one based on the the values of "
                   "'home-dir-prefix' and 'home-dir-template'.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="HomeDirPrefix", subkey='Instance', instance=instance),
        }, {
            "name": "home-dir-template",
            "description": "Home directory template",
            "doc": "When the unix home directory is not entered into Active "
                   "Directory, OneFS will generate one based on the the values of "
                   "'home-dir-prefix' and 'home-dir-template'.  This setting accepts "
                   "several variables which are expanded when generating the name. "
                   "'%H' is replaced with the 'home-dir-prefix'. '%L' is replaced "
                   "with the current hostname of the node. '%D' is replaced with "
                   "the NetBIOS name of the user's domain, normalized to upper-case. "
                   "'%U' is replaced with the user's name, normalized to lower-case.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="HomeDirTemplate", subkey='Instance', instance=instance),
        }, {
            "name": "home-dir-umask",
            "description": "Home directory umask",
            "doc": "When creating a user's home directory, this setting determines "
                   "the umask to use when calculating the mode.  The umask is used "
                   "to exclude permissions which would otherwise be set.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="HomeDirUmask", subkey='Instance', instance=instance),
            "hidden": True
        }, {
            "name": "ldap-sign-and-seal",
            "description": "Ldap Sign and Seal",
            "doc": "Lsassd attempts to automatically negotiate the security when "
                   "connecting to a Domain Controller over LDAP (ports 389 and "
                   "3268).  If the LDAP connection requires additional security or "
                   "negotiation fails, this setting instructs lsassd to encrypt "
                   "the LDAP connection.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="LdapSignAndSeal", subkey='Instance', instance=instance),
        }, {
            "name": "login-shell-template",
            "description": "Login shell template",
            "doc": "When the unix login shell is not entered into Active Directory, "
                   "OneFS will assign the value of this setting. If this value is "
                   "not set to a valid shell on OneFS, access to certain services "
                   "(ftp, scp, etc) will be denied.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="LoginShellTemplate", subkey='Instance', instance=instance),
        }, {
            "name": "machine-password-lifespan",
            "description": "Maximum age of the password lifespan (in seconds)",
            "doc": "OneFS will periodically change the shared secret between the "
                   "Active Directory domain and the cluster.  This setting controls "
                   "the maximum age of the password.  This period should be shorter "
                   "than any domain policy.  If the cluster detects the password is "
                   "set to not expire, the machine password will not be changed "
                   "automatically.  In that case, rerunning the domain join "
                   "process will cause us to reset the password.",
            "cclass": CONFIG_CLASS_AD,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_AD,
                key="MachinePasswordLifespan", subkey='Instance', instance=instance),
        }, {
            "name": "nss-enumeration-enabled",
            "description": "Enable responses to NSS queries",
            "doc": "Return Active Directory users and groups via the standard unix "
                   "functions such as getpwnam, getgrnam, etc.  This setting is "
                   "required for compatibility with unix services.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="NssEnumerationEnabled", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "http-keytab-path",
            "description": "Generated keytab file for HTTP server",
            "doc": "Lsassd generates a special keytab for use by HTTP with restricted "
                   "permissions.  This setting controls the location of the file.",
            "cclass": CONFIG_CLASS_AD,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_AD,
                key="HttpKeytabPath", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "store-sfu-mappings",
            "description": "Store mappings retrieved from SFU instead of just caching",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="StoreSFUMappings", subkey='Instance', instance=instance),
        }, {
            "name": "ignored-trusted-domains",
            "description": "Ignored Trusted Domains",
            "doc": "OneFS can be configured to ignore certain trusted domains.  "
                   "These domains will not be available on the cluster.",
            "cclass": CONFIG_CLASS_AD,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_AD,
                key="DomainManagerExcludeTrustsList", subkey='Instance', instance=instance),
        }, {
            "name": "include-trusted-domains",
            "description": "Include Trusted Domains",
            "doc": "OneFS can be configured to include only certain trusted domains.  "
                   "These domains will be available on the cluster.",
            "cclass": CONFIG_CLASS_AD,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_AD,
                key="DomainManagerIncludeTrustsList", subkey='Instance', instance=instance),
        }, {
            "name": "ignore-all-trusts",
            "description": "Ignore all trusted domains",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="DomainManagerIgnoreAllTrusts", subkey='Instance', instance=instance),
        }, {
             "name": "ad-authentication-enabled",
             "description": "Enable the Active Directory provider to respond to "
                            "PAM authentication requests",
             "doc": "This setting controls whether Active Directory is used for PAM "
                    "authentication.  When false, AD users will be prevented from "
                    "logging in via the WebUI or console.",
             "weblabel": "Authentication enabled",
             "cclass": CONFIG_CLASS_AD,
             "type": BOOL_TYPE,
             "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                 key="AuthEnabled", subkey='Instance', instance=instance),
        }, {
            "name": "domain-offline-alerts",
            "description": "Enable alerts when a domain goes offline.",
            "doc": "OneFS has the ability to notify when we can't access an "
                "Active Directory domain.  This setting controls whether or "
                "not an event is raised.",
            "weblabel": "Offline Domain Alerts",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="AlertsEnabled", subkey='Instance', instance=instance),
        }, {
            "name": "allocate-uids",
            "description": "Allocate uids for AD users",
            "doc": "Even though OneFS does not require a user to have a UID assigned, "
                   "one is normally assigned to all accounts automatically for unix "
                   "compatibility.  This setting can disable this functionality but "
                   "will cause compatibility issues with unix services.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="AllocateUids", subkey='Instance', instance=instance),
        }, {
            "name": "allocate-gids",
            "description": "Allocate gids for AD groups",
            "doc": "Even though OneFS does not require a group to have a GID "
                   "assigned, one is normally assigned to all groups automatically "
                   "for unix compatibility.  This setting can disable this "
                   "functionality but will cause compatibility issues with unix "
                   "services.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="AllocateGids", subkey='Instance', instance=instance),
        }, {
            "name": "lookup-users",
            "description": "lookup users before allocating a uid",
            "doc": "Before resorting to allocating a UID for a user, OneFS "
                   "automatically searches the local and unix sources for accounts "
                   "that match by name.  If such an account is found, its UID is "
                   "used.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="LookupUsers", subkey='Instance', instance=instance),
        }, {
            "name": "lookup-groups",
            "description": "lookup groups before allocating a gid",
            "doc": "Before resorting to allocating a GID for a group, OneFS "
                   "automatically searches the local and unix sources for groups "
                   "that match by name.  If such an account is found, its GID is "
                   "used.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="LookupGroups", subkey='Instance', instance=instance),
        }, {
            "name": "lookup-normalize-users",
            "description": "Normalize the user name to lower case before lookup",
            "doc": "This setting affects the behavior of 'lookup-users' by "
                   "normalizing the user's name to lower-case before searching. "
                   "This could be undesirable if a source contains case sensitive "
                   "names.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="LookupNormalizeUsers", subkey='Instance', instance=instance),
        }, {
            "name": "lookup-normalize-groups",
            "description": "Normalize the group name to lower case before lookup",
            "doc": "This setting affects the behavior of 'lookup-group' by "
                   "normalizing the group's name to lower-case before searching. "
                   "This could be undesirable if a source contains case sensitive "
                   "names.",
            "cclass": CONFIG_CLASS_AD,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_AD,
                key="LookupNormalizeGroups", subkey='Instance', instance=instance),
        }, {
            "name": "lookup-domains",
            "description": "Limit user and group lookup to the domains listed.",
            "doc": "When lookup-users and/or lookup-groups are configured, this "
                   "setting controls which accounts we will attempt to lookup. "
                   "By default, only accounts in the primary active directory "
                   "domain are looked up.",
            "cclass": CONFIG_CLASS_AD,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_AD,
                key="LookupDomains", subkey='Instance', instance=instance),
        }]

libNis  = [ {
            "name": "nis-nis-domain",
            "description": "NIS domain",
            "weblabel": "Domain",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS, key="NisDomain",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-retry-time",
            "description": "Timeout period after which a request will be retried",
            "weblabel": "Request retry period",
            "cclass": CONFIG_CLASS_NIS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_NIS, key="RetryTime",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-request-timeout",
            "description": "Timeout period after which a request will not be retried and will fail",
            "weblabel": "Request timeout period",
            "cclass": CONFIG_CLASS_NIS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_NIS, key="RequestTime",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-check-interval",
            "description": "Duration between checks for valid and invalid servers",
            "weblabel": "Server check interval",
            "cclass": CONFIG_CLASS_NIS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_NIS, key="CheckInterval",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-server",
            "description": "Comma separated list of NIS servers",
            "weblabel": "Server(s)",
            "cclass": CONFIG_CLASS_NIS,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfMultiStringValidator(path=REGPATH_NIS, key="Servers",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-hostname-lookup-enabled",
            "description": "Enable hostname lookups for this instance of the nis-provider",
            "weblabel": "Hostname lookups enabled",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="HostLookupEnabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-balance-servers",
            "description": "Enable the nis-provider to affinitize to a random server",
            "weblabel": "Balance servers",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="BalanceServers", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-enabled",
            "description": "Enable the nis-provider",
            "weblabel": "Provider enabled",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="Enabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-authentication-enabled",
            "description": "Enable the provider to respond to authentication requests",
            "weblabel": "Authentication enabled",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="AuthEnabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-enumerate-groups",
            "description": "Enable the nis-provider to respond to getgrent requests",
            "weblabel": "Enumerate groups",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="EnumerateGroups", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-enumerate-users",
            "description": "Enable the nis-provider to respond to getpwent requests",
            "weblabel": "Enumerate users",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="EnumerateUsers", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-cache-entry-expiry",
            "description": "Amount of time to cache a user/group",
            "weblabel": "Cache Entry Expiry",
            "cclass": CONFIG_CLASS_NIS,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_NIS,
                key="CacheEntryExpiry", range=(0,60*60*24),
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-domain",
            "description": "Alternate Domain to use for NIS users/group",
            "weblabel": "Alternate Domain",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="Domain", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-group-domain",
            "description": "Domain name used to refer to NIS groups.  "
                "The default is NIS_GROUPS",
            "weblabel": "Group Domain",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="GroupDomain", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "nis-ntlm-support",
            "description": "For users with NTLM-compatible credentials, "
                "this setting controls what NTLM versions to support.",
            "weblabel": "NTLM Support",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="NTLMSupport", subkey='Instance', instance=instance,
                valid=['all', 'v2only', 'none']),
            "hidden": False,
        }, {
            "name": "nis-normalize-groups",
            "description": "Normalize groups to lowercase before looking up",
            "weblabel": "Normalize Groups",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_NIS,
                key="NormalizeGroups", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "nis-normalize-users",
            "description": "Normalize usernames to lowercase before looking up",
            "weblabel": "Normalize Users",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_NIS,
                key="NormalizeUsers", subkey='Instance', instance=instance),
        }, {
            "name": "listable-users",
            "description": "List of users nis-provider will return via getpwent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS, key="ListAllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unlistable-users",
            "description": "List of users nis-provider will not return via getpwent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS, key="ListDenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "listable-groups",
            "description": "List of groups nis-provider will return via getgrent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="ListAllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unlistable-groups",
            "description": "List of groups nis-provider will not return via getgrent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="ListDenyGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "findable-users",
            "description": "List of users nis-provider will return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS, key="AllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unfindable-users",
            "description": "List of users nis-provider will not return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS, key="DenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "findable-groups",
            "description": "List of groups nis-provider will return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="AllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unfindable-groups",
            "description": "List of groups nis-provider will not return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="DenyGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-listable",
            "description": "Restrict the user and group lists to "
                           "entries in list-users and list-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="RestrictList", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-findable",
            "description": "Restrict the users and groups that can be "
                           "resolved and authenticated to entries in "
                           "allow-users and allow-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_NIS,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_NIS,
                key="RestrictAllow", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "nis-user-domain",
            "description": "Domain name used to refer to NIS users.  "
                "The default is NIS_USERS",
            "weblabel": "User Domain",
            "cclass": CONFIG_CLASS_NIS,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_NIS,
                key="UserDomain", subkey='Instance', instance=instance),
            "hidden": True,
        },
        ]

libLdap = [
       {
            "name": "ldap-base-dn",
            "description": "Distinguished name of the entry at which to start the LDAP search",
            "weblabel": "Base distinguished name",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="BaseDn",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-bind-dn",
            "description": "Distinguished name of the entry used to bind to the LDAP server",
            "weblabel": "Bind distinguished name",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="BindDn",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-bind-mechanism",
            "description": "Mechanism used to bind to the LDAP server",
            "cclass": CONFIG_CLASS_LDAP,
            "type": ENUM_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                 key="BindMechanism", valid=["simple","gssapi","digest-md5"],
                 subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "ldap-bind-password",
            "description": "Password used when binding to the LDAP server",
            "weblabel": "Bind password",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="BindPw",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-bind-timeout",
            "description": "Bind timeout period",
            "weblabel": "Bind timeout period",
            "cclass": CONFIG_CLASS_LDAP,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LDAP, key="BindTimeout",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-search-timeout",
            "description": "Search timeout period",
            "weblabel": "Search timeout period",
            "cclass": CONFIG_CLASS_LDAP,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LDAP, key="SearchTimeout",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-search-scope",
            "description": "Search scope",
            "weblabel": "Search scope",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="SearchScope", subkey='Instance', instance=instance,
                valid=['base', 'onelevel', 'subtree', 'children']),
            "hidden": False,
        }, {
            "name": "ldap-check-interval",
            "description": "Duration between checks for valid and invalid servers",
            "weblabel": "Server check interval",
            "cclass": CONFIG_CLASS_LDAP,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LDAP, key="CheckInterval",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-server-uri",
            "description": "Comma separated list of LDAP server URIs",
            "weblabel": "Server URI(s)",
            "cclass": CONFIG_CLASS_LDAP,
            "type": MULTI_SZ_TYPE,
            "validator": LWRegGconfLdapServerMultiStringValidator(path=REGPATH_LDAP, key="URI",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-ignore-tls-errors",
            "description": "Set the ldap-provider to ignore all TLS errors",
            "weblabel": "Ignore TLS errors",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP, key="IgnoreTlsErrors",
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-balance-servers",
            "description": "Enable the ldap-provider to affinitize to a random server",
            "weblabel": "Balance servers",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="BalanceServers", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-enabled",
            "description": "Enable the ldap-provider",
            "weblabel": "Provider enabled",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="Enabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-authentication-enabled",
            "description": "Enable the provider to respond to authentication requests",
            "weblabel": "Authentication enabled",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="AuthEnabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-enumerate-groups",
            "description": "Enable the ldap-provider to respond to getgrent requests",
            "weblabel": "Enumerate groups",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="EnumerateGroups", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-enumerate-users",
            "description": "Enable the ldap-provider to respond to getpwent requests",
            "weblabel": "Enumerate users",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="EnumerateUsers", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-cache-entry-expiry",
            "description": "Amount of time to cache a user/group",
            "weblabel": "Cache Entry Expiry",
            "cclass": CONFIG_CLASS_LDAP,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LDAP,
                key="CacheEntryExpiry", range=(0,60*60*24),
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-domain",
            "description": "Alternate Domain to use for LDAP users/group",
            "weblabel": "Alternate Domain",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="Domain", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-group-domain",
            "description": "Domain name used to refer to LDAP groups.  "
                "The default is LDAP_GROUPS.",
            "weblabel": "Group Domain",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="GroupDomain", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "ldap-ntlm-support",
            "description": "For users with NTLM-compatible credentials, "
                "this setting controls what NTLM versions to support.",
            "weblabel": "NTLM Support",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="NTLMSupport", subkey='Instance', instance=instance,
                valid=['all', 'v2only', 'none']),
            "hidden": False,
        }, {
            "name": "ldap-normalize-groups",
            "description": "Normalize groups to lowercase before looking up",
            "weblabel": "Normalize Groups",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LDAP,
                key="NormalizeGroups", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-normalize-users",
            "description": "Normalize usernames to lowercase before looking up",
            "weblabel": "Normalize Users",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_LDAP,
                key="NormalizeUsers", subkey='Instance', instance=instance),
        }, {
            "name": "listable-users",
            "description": "List of users ldap-provider will return via getpwent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="ListAllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unlistable-users",
            "description": "List of users ldap-provider will not return via getpwent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="ListDenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "listable-groups",
            "description": "List of groups ldap-provider will return via getgrent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="ListAllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unlistable-groups",
            "description": "List of groups ldap-provider will not return via getgrent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="ListDenyGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "findable-users",
            "description": "List of users ldap-provider will return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="AllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unfindable-users",
            "description": "List of users ldap-provider will not return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP, key="DenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "findable-groups",
            "description": "List of groups ldap-provider will return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="AllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unfindable-groups",
            "description": "List of groups ldap-provider will not return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="DenyGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-listable",
            "description": "Restrict the user and group lists to "
                           "entries in list-users and list-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="RestrictList", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-findable",
            "description": "Restrict the users and groups that can be "
                           "resolved and authenticated to entries in "
                           "allow-users and allow-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="RestrictAllow", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "ldap-user-domain",
            "description": "Domain name used to refer to LDAP users.  "
                "The default is LDAP_USERS.",
            "weblabel": "User Domain",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="UserDomain", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "ldap-require-secure-connection",
            "description": "Require a secure connection when binding with a password "
                           "or retrieving password related attributes",
            "weblabel": "Secure connection required",
            "cclass": CONFIG_CLASS_LDAP,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_LDAP,
                key="RequireSecure", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
             "name": "ldap-certificate-authority-file",
             "description": "PEM file containing the certificates of trusted certificate authorities",
             "weblabel": "Certificate authorities",
             "cclass": CONFIG_CLASS_LDAP,
             "type": FILE_TYPE,
             "validator": LWRegGconfFileValidator(path=REGPATH_LDAP, key="CACertFile",
                 subkey='Instance', instance=instance),
             "hidden": False,
        }, {
            "name": "ldap-uid-attribute",
            "description": "LDAP uidNumber attribute",
            "weblabel": "uidNumber attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="uidNumber", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-gid-attribute",
            "description": "LDAP gidNumber attribute",
            "weblabel": "gidNumber attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="gidNumber", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-gecos-attribute",
            "description": "LDAP gecos attribute",
            "weblabel": "gecos attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="gecos", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-homedir-attribute",
            "description": "LDAP homeDirectory attribute",
            "weblabel": "homeDirectory attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="homeDirectory", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-shell-attribute",
            "description": "LDAP loginShell attribute",
            "weblabel": "loginShell attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="loginShell", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-group-members-attribute",
            "description": "LDAP memberUid attribute",
            "weblabel": "memberUid attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="memberUid", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-name-attribute",
            "description": "LDAP uid attribute",
            "weblabel": "uid attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="uid", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-cn-attribute",
            "description": "LDAP cn attribute",
            "weblabel": "cn attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="cn", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-email-attribute",
            "description": "LDAP email attribute",
            "weblabel": "email attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="email", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-user-filter",
            "description": "LDAP filter for user objects",
            "weblabel": "user filter",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="UserFilter", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-group-filter",
            "description": "LDAP filter for group objects",
            "weblabel": "group filter",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="GroupFilter", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-netgroup-filter",
            "description": "LDAP filter for netgroups objects",
            "weblabel": "netgroup filter",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="NetgroupFilter", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-nt-password-attribute",
            "description": "LDAP ntPasswdHash attribute",
            "weblabel": "ntPasswdHash attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="ntPasswdHash", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-crypt-password-attribute",
            "description": "LDAP cryptPasswd attribute",
            "weblabel": "cryptPasswd attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="cryptPasswd", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-unique-group-members-attribute",
            "description": "LDAP uniqueMember attribute",
            "weblabel": "uniqueMember attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="uniqueMember", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-netgroup-triple-attribute",
            "description": "LDAP NIS netgroup triple",
            "weblabel": "netgroup triple",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="nisNetgroupTriple", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-netgroup-members-attribute",
            "description": "LDAP Member NIS netgroup",
            "weblabel": "netgroup attribute",
            "cclass": CONFIG_CLASS_LDAP_ATTRIB,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="memberNisNetgroup", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-user-base-dn",
            "description": "Distinguished name of the entry at which to start "
                "the LDAP search for users.",
            "weblabel": "User base distinguished name",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="UserBaseDn", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "ldap-group-base-dn",
            "description": "Distinguished name of the entry at which to start "
                "the LDAP search for groups.",
            "weblabel": "Group base distinguished name",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="GroupBaseDn", subkey='Instance', instance=instance),
        }, {
            "name": "ldap-netgroup-base-dn",
            "description": "Distinguished name of the entry at which to start "
                "the LDAP search for netgroups.",
            "weblabel": "Netgroup base distinguished name",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="NetgroupBaseDn", subkey='Instance', instance=instance),
        }, {
            "name": "ldap-user-search-scope",
            "description": "Search scope for users.",
            "weblabel": "User search scope",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="UserSearchScope", subkey='Instance', instance=instance,
                valid=['default', 'base', 'onelevel', 'subtree',
                    'children']),
            "hidden": False
        }, {
            "name": "ldap-group-search-scope",
            "description": "Search scope for groups.",
            "weblabel": "Group search scope",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="GroupSearchScope", subkey='Instance',
                instance=instance, valid=['default', 'base', 'onelevel',
                    'subtree', 'children']),
            "hidden": False
        }, {
            "name": "ldap-netgroup-search-scope",
            "description": "Search scope for netgroups.",
            "weblabel": "Netgroup search scope",
            "cclass": CONFIG_CLASS_LDAP,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_LDAP,
                key="NetgroupSearchScope", subkey='Instance',
                instance=instance, valid=['default', 'base', 'onelevel',
                    'subtree', 'children']),
            "hidden": False
        }]


libfile = [{
            "name": "password-file",
            "description": "Supplemental password file",
            "doc": "OneFS provides the ability to use an additional file as a source "
                   "of user information.  This file should be formated as a dbm "
                   "file and usually has the name spwd.db.  Lsassd automatically "
                   "filters information on insecure accesses.  The path should "
                   "be accessible on all nodes.",
            "cclass": CONFIG_CLASS_FILE,
            "type": FILE_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="PasswdFile", subkey='Instance', instance=instance),
        }, {
            "name": "group-file",
            "description": "Group replacement file",
            "doc": "OneFS provides the ability to use an additional file as a source "
                   "of group information.  This file should be formatted the same "
                   "as the /etc/group file and should accessible on all nodes.",
            "cclass": CONFIG_CLASS_FILE,
            "type": FILE_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="GroupFile",
                subkey='Instance', instance=instance),
        }, {
            "name": "netgroup-file",
            "description": "Netgroup replacement file",
            "doc": "OneFS provides the ability to use an additional file as a source "
                   "of netgroup information.  This file should be formatted the same "
                   "as the /etc/netgroup file and should accessible on all nodes.",
            "cclass": CONFIG_CLASS_FILE,
            "type": FILE_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="NetgroupFile",
                subkey='Instance', instance=instance),
        }, {
            "name": "file-enabled",
            "description": "Enable the file-provider",
            "weblabel": "Provider enabled",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="Enabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "listable-users",
            "description": "List of users file-provider will return via getpwent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="ListAllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unlistable-users",
            "description": "List of users file-provider will filter via getpwent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="ListDenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "listable-groups",
            "description": "List of groups file-provider will return via getgrent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="ListAllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unlistable-groups",
            "description": "List of groups file-provider will filter via getgrent requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="ListDenyGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "modifiable-users",
            "description": "List of users file-provider allow to be modified",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="ModAllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unmodifiable-users",
            "description": "List of users file-provider will not allow to be modified",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="ModDenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "modifiable-groups",
            "description": "List of groups file-provider will allow to be modified",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="ModAllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unmodifiable-groups",
            "description": "List of groups file-provider will not allow to be modified",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="ModDenyGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "findable-users",
            "description": "List of users file-provider will return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="AllowUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unfindable-users",
            "description": "List of users file-provider will not return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE, key="DenyUsers",
                subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "findable-groups",
            "description": "List of groups file-provider will return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="AllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "unfindable-groups",
            "description": "List of groups file-provider will not return via find requests",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="AllowGroups", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-listable",
            "description": "Restrict the user and group lists to "
                           "entries in list-users and list-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="RestrictList", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-modifiable",
            "description": "Restrict the ability to modify users and groups "
                           "to entries in list-users and list-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="RestrictMod", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "restrict-findable",
            "description": "Restrict the users and groups that can be "
                           "resolved and authenticated to entries in "
                           "allow-users and allow-groups",
            "doc": "",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="RestrictAllow", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "file-authentication-enabled",
            "description": "Enable the provider to respond to authentication requests",
            "weblabel": "Authentication enabled",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="AuthEnabled", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "enumerate-groups",
            "description": "Enable the file-provider to respond to getgrent requests",
            "weblabel": "Enumerate groups",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="EnumerateGroups", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "enumerate-users",
            "description": "Enable the file-provider to respond to getpwent requests",
            "weblabel": "Enumerate users",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfBooleanValidator(path=REGPATH_FILE,
                key="EnumerateUsers", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "file-cache-entry-expiry",
            "description": "Amount of time to cache a user/group",
            "weblabel": "Cache Entry Expiry",
            "cclass": CONFIG_CLASS_FILE,
            "type": DWORD_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_FILE,
                key="CacheEntryExpiry", range=(0,60*60*24),
                subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "file-domain",
            "description": "Alternate Domain to use for file users/group",
            "weblabel": "Alternate Domain",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="Domain", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "file-group-domain",
            "description": "Domain name used to refer to file groups.  "
                "The default is FILE_GROUPS",
            "weblabel": "Group Domain",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="GroupDomain", subkey='Instance', instance=instance),
            "hidden": True,
        }, {
            "name": "file-ntlm-support",
            "description": "For users with NTLM-compatible credentials, "
                "this setting controls what NTLM versions to support.",
            "weblabel": "NTLM Support",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="NTLMSupport", subkey='Instance', instance=instance,
                valid=['all', 'v2only', 'none']),
            "hidden": False,
        }, {
            "name": "file-normalize-groups",
            "description": "Normalize groups to lowercase before looking up",
            "weblabel": "Normalize Groups",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_FILE,
                key="NormalizeGroups", subkey='Instance', instance=instance),
            "hidden": False,
        }, {
            "name": "file-normalize-users",
            "description": "Normalize usernames to lowercase before looking up",
            "weblabel": "Normalize Users",
            "cclass": CONFIG_CLASS_FILE,
            "type": BOOL_TYPE,
            "validator": LWRegGconfLongValidator(path=REGPATH_FILE,
                key="NormalizeUsers", subkey='Instance', instance=instance),
        }, {
            "name": "file-user-domain",
            "description": "Domain name used to refer to file users.  "
                "The default is NIS_USERS",
            "weblabel": "User Domain",
            "cclass": CONFIG_CLASS_FILE,
            "type": SZ_TYPE,
            "validator": LWRegGconfStringValidator(path=REGPATH_FILE,
                key="UserDomain", subkey='Instance', instance=instance),
            "hidden": True,
        }]

def nameMangle(config, configName):
	nameField = config["name"]
	nameField = nameField.replace("%s-" % configName, "", 1)
	if(config["type"] == BOOL_TYPE):
		nameField = nameField.replace("-enabled", "")
	nameField = nameField.replace("-","_")
	return nameField

def schemaTypes(config):
	type = None
	multiple = False
	if(hasattr(config["validator"],"valid")):
		if(config["validator"].valid is not None):
			type = 'STRING('
			for str in config["validator"].valid:
				if multiple:
					type += ', '
				type += '"'+str+'"'
				multiple = True
			type += ')'
	if type is None:
		type = schemaDic[config["type"]]
		
	return type


class do():
    def work(self, lib, configName):
		#print config header
		separator = ""
		for i in range(1 , 80):
			separator += "*"
			
		print "%s\n* %s Config\n%s\n " % (separator, configName, separator)

		#Parse lib
		lib = sorted(lib, key=lambda entry: entry["name"].replace("%s-" %configName,"",1))
		for x in lib:
			#do work if has valid parameters
			if(hasattr(x["validator"],"key")):
				
				hasStringValidator = False
				hasIntValidator = False

				nameField = nameMangle(x, configName)

				#create string types
				if(hasattr(x["validator"],"valid")):
					if(x["validator"].valid is not None):
						hasStringValidator = True
						print "static const char *%s_strs[] = {" % (nameField)

						for strn in x["validator"].valid:
							print '\t"%s",' % (strn)

						print "\tNULL,\n};\n"

				#create int types
				if(hasattr(x["validator"],"range")):
					if(x["validator"].range is not None):
						hasIntValidator = True
						print "static const uint32_t %s_range[] = { %d, %d };" % (nameField,x["validator"].range[0], x["validator"].range[1])

				#print struct mold
				if(hasattr(x["validator"],"key")):
					print '%s_INSTANCE_PARAM(%s_PARAM_%s,\n\t.name = "%s",\n\t.key = "%s",\n\t.type = %s,' % (configName.upper(), configName.upper(), nameField.upper(), nameField, x["validator"].key, dic[x["type"]])

				#add conditional components
				if (hasStringValidator):
					print "\t.validator = &lwc_string_enum_validator,\n\t.validation_ctx = %s_strs," % (nameField)

				if(hasIntValidator):
					print "\t.validator = &lwc_int_range_validator,\n\t.validation_ctx = %s_range," % (nameField)

				print ");\n"
			else:
				print "****%s/%s does not have valid formatting\n" % (configName, x["name"])

		print "const struct lwc_reg_def *%s_INSTANCE_CONFIG_DEF[] = {" % (configName.upper())
		for x in lib:
			if(hasattr(x["validator"],"key")):
				nameField = nameMangle(x, configName)
				print '\t&%s_PARAM_%s,' % ( configName.upper(), nameField.upper())
		print "};"
		
		#print out spec list
		print "%s\n* %s Spec\n%s\n " % (separator, configName, separator)
		for x in lib:
			nameField = nameMangle(x, configName)
			print "\t%s: %s," % (nameField, typeDic[x["type"]])

		#print out m4 schema (results require some manual manipulation)
		print "%s\n* %s Schema\n%s\n " % (separator, configName, separator)
		print "define(`PUT_%s', `OBJECT(" % (configName.upper())
		print "    `\"name\" : STRING',"
		size = len(lib)
		for x in lib:
			nameField = nameMangle(x, configName)
			size = size -1
			print "    `\"%s\" : DEFAULTABLE(`%s')'%s" % (nameField, schemaTypes(x),
			    ',' if size is not 0 else '')
		print "    )'\n)"

		print "define(`POST_%s', `OBJECT(" % (configName.upper())
		print "    `\"name\" : REQUIRED STRING',"
		size = len(lib)
		for x in lib:
			nameField = nameMangle(x, configName)
			size = size -1
			print "    `\"%s\" : %s'%s" % (nameField, schemaTypes(x),
			    ',' if size is not 0 else '')
		print "    )'\n)"

		print "define(`GET_%s', `OBJECT(" % (configName.upper())
		print "    `\"name\" : REQUIRED STRING',"
		print "    `\"id\" : REQUIRED STRING',"
		size = len(lib)
		for x in lib:
			nameField = nameMangle(x, configName)
			size = size -1
			print "    `\"%s\" : REQUIRED %s'%s" % (nameField, schemaTypes(x),
			    ',' if size is not 0 else '')
		print "    )'\n)"

    def makesys(self, lib, configname):
 		lib = sorted(lib, key=lambda entry: entry["name"].replace("-","_"))
		for x in lib:
			name = x["name"].replace("-","_")
			if (not hasattr(x["validator"],"key")):
				if (not isinstance(x["validator"],IdmapValidator)):
					if (x["type"] ==  SZ_TYPE):
						union_type = "sz"
						def_val = '"%s"' % x["validator"].default
					elif(x["type"] == DWORD_TYPE):
						union_type = "dword"
						def_val = x["validator"].default
					elif(x["type"] == BOOL_TYPE):
						union_type = "boolean"
						def_val = x["validator"].default

					print 'struct lwc_data %s_def_val = {\n\t .type = %s\n\t .value = { .%s = %s }\n};' % (name,dic[x["type"]], union_type ,def_val)
					print '%s_SYS_PARAM(GLOBAL_SYS_CTRL_%s,\n\t.name = "%s"\n\t.path = "%s"\n\t.default_value = &%s_def_val\n);' % (configname.upper(), name.upper(), name, x["validator"].sysctl, name)

		print "\n\nconst struct lwc_sysctl_def *GLOBAL_SYS_CTRL_DEF[] = {"
		for x in lib:
			if(not hasattr(x["validator"],"key")):	
				name = x["name"].replace('-','_')
				print "\t&GLOBAL_SYS_CTRL_%s," % name.upper()
		print "};"


    def makeM4GET(self, lib, configname):
        lib = sorted(lib, key=lambda entry: entry["name"].replace("-","_"))

        print "define(`GET_%s', `OBJECT(" % configname.upper()

        for x in lib:
           name = x["name"].replace("-","_")

           print '    `"%s" : DEFAULTABLE(`%s\')\',' % (name, schemaDic[x["type"]])

        print "    )'\n)"


worker = do()

worker.work(libAd, "ad")
worker.work(libGlobal, "global")
worker.makesys(libGlobal, "global")
worker.makeM4GET(libGlobal, "global")
worker.work(libfile, "file")
worker.work(libLdap, "ldap")
worker.work(libLocal, "local")
worker.work(libNis, "nis")
worker.work(libZone, "zone")
 

