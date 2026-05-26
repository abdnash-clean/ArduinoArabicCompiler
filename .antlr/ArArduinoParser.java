// Generated from e:/projects/ArduinoArabicCompiler/ArArduinoParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ArArduinoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, IF=2, ELSE=3, WHILE=4, TRUE=5, FALSE=6, INT_T=7, FLOAT_T=8, VOID=9, 
		FUNCTION=10, RETURN=11, SETUP=12, LOOP=13, BOOL=14, ASSIGN=15, PLUS=16, 
		MINUS=17, MUL=18, DIV=19, GTE=20, LTE=21, EQ=22, NEQ=23, GT=24, LT=25, 
		OR=26, AND=27, LPAREN=28, RPAREN=29, LBRACE=30, RBRACE=31, COLON=32, SEMI=33, 
		COMA=34, NUMBER=35, ID=36, WS=37, LINE_COMMENT=38;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_varDecl = 2, RULE_funDecl = 3, 
		RULE_funcBody = 4, RULE_params = 5, RULE_param = 6, RULE_block = 7, RULE_statement = 8, 
		RULE_idStatement = 9, RULE_idSuffix = 10, RULE_ifStat = 11, RULE_whileStat = 12, 
		RULE_returnStat = 13, RULE_args = 14, RULE_expression = 15, RULE_orExpr = 16, 
		RULE_andExpr = 17, RULE_relExpr = 18, RULE_relOp = 19, RULE_addExpr = 20, 
		RULE_mulExpr = 21, RULE_unaryExpr = 22, RULE_primary = 23, RULE_primaryIdSuffix = 24, 
		RULE_type = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "varDecl", "funDecl", "funcBody", "params", 
			"param", "block", "statement", "idStatement", "idSuffix", "ifStat", "whileStat", 
			"returnStat", "args", "expression", "orExpr", "andExpr", "relExpr", "relOp", 
			"addExpr", "mulExpr", "unaryExpr", "primary", "primaryIdSuffix", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\u0645\\u062A\\u063A\\u064A\\u0631'", null, null, "'\\u0637\\u0627\\u0644\\u0645\\u0627'", 
			"'\\u0635\\u062D'", "'\\u063A\\u0644\\u0637'", "'\\u0635\\u062D\\u064A\\u062D'", 
			"'\\u0639\\u0634\\u0631\\u064A'", "'\\u0641\\u0627\\u0631\\u063A'", "'\\u062F\\u0627\\u0644\\u0629'", 
			"'\\u0627\\u0631\\u062C\\u0639'", "'\\u0625\\u0639\\u062F\\u0627\\u062F'", 
			"'\\u062A\\u0643\\u0631\\u0627\\u0631'", "'\\u0645\\u0646\\u0637\\u0642\\u064A'", 
			"'='", "'+'", "'-'", "'*'", "'/'", "'>='", "'<='", "'=='", "'!='", "'>'", 
			"'<'", "'\\u0623\\u0648'", "'\\u0648'", "'('", "')'", "'{'", "'}'", "':'", 
			"'\\u061B'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "IF", "ELSE", "WHILE", "TRUE", "FALSE", "INT_T", "FLOAT_T", 
			"VOID", "FUNCTION", "RETURN", "SETUP", "LOOP", "BOOL", "ASSIGN", "PLUS", 
			"MINUS", "MUL", "DIV", "GTE", "LTE", "EQ", "NEQ", "GT", "LT", "OR", "AND", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI", "COMA", "NUMBER", 
			"ID", "WS", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ArArduinoParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ArArduinoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ArArduinoParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR || _la==FUNCTION) {
				{
				{
				setState(52);
				declaration();
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(58);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public FunDeclContext funDecl() {
			return getRuleContext(FunDeclContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(62);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				varDecl();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 2);
				{
				setState(61);
				funDecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(ArArduinoParser.VAR, 0); }
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(ArArduinoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ArArduinoParser.SEMI, 0); }
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(VAR);
			setState(65);
			match(ID);
			setState(66);
			match(COLON);
			setState(67);
			type();
			setState(68);
			match(ASSIGN);
			setState(69);
			expression();
			setState(70);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunDeclContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(ArArduinoParser.FUNCTION, 0); }
		public FuncBodyContext funcBody() {
			return getRuleContext(FuncBodyContext.class,0);
		}
		public FunDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funDecl; }
	}

	public final FunDeclContext funDecl() throws RecognitionException {
		FunDeclContext _localctx = new FunDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_funDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(FUNCTION);
			setState(73);
			funcBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncBodyContext extends ParserRuleContext {
		public TerminalNode SETUP() { return getToken(ArArduinoParser.SETUP, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TerminalNode VOID() { return getToken(ArArduinoParser.VOID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode LOOP() { return getToken(ArArduinoParser.LOOP, 0); }
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public FuncBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcBody; }
	}

	public final FuncBodyContext funcBody() throws RecognitionException {
		FuncBodyContext _localctx = new FuncBodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcBody);
		int _la;
		try {
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SETUP:
				enterOuterAlt(_localctx, 1);
				{
				setState(75);
				match(SETUP);
				setState(76);
				match(LPAREN);
				setState(77);
				match(RPAREN);
				setState(78);
				match(COLON);
				setState(79);
				match(VOID);
				setState(80);
				block();
				}
				break;
			case LOOP:
				enterOuterAlt(_localctx, 2);
				{
				setState(81);
				match(LOOP);
				setState(82);
				match(LPAREN);
				setState(83);
				match(RPAREN);
				setState(84);
				match(COLON);
				setState(85);
				match(VOID);
				setState(86);
				block();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(87);
				match(ID);
				setState(88);
				match(LPAREN);
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(89);
					params();
					}
				}

				setState(92);
				match(RPAREN);
				setState(93);
				match(COLON);
				setState(94);
				type();
				setState(95);
				block();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(ArArduinoParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ArArduinoParser.COMA, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			param();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(100);
				match(COMA);
				setState(101);
				param();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public TerminalNode COLON() { return getToken(ArArduinoParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(ID);
			setState(108);
			match(COLON);
			setState(109);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(ArArduinoParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ArArduinoParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(LBRACE);
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 68719478806L) != 0)) {
				{
				{
				setState(112);
				statement();
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(118);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public IdStatementContext idStatement() {
			return getRuleContext(IdStatementContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ArArduinoParser.SEMI, 0); }
		public IfStatContext ifStat() {
			return getRuleContext(IfStatContext.class,0);
		}
		public WhileStatContext whileStat() {
			return getRuleContext(WhileStatContext.class,0);
		}
		public ReturnStatContext returnStat() {
			return getRuleContext(ReturnStatContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statement);
		try {
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				varDecl();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				idStatement();
				setState(122);
				match(SEMI);
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(124);
				ifStat();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(125);
				whileStat();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 5);
				{
				setState(126);
				returnStat();
				setState(127);
				match(SEMI);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdStatementContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public IdSuffixContext idSuffix() {
			return getRuleContext(IdSuffixContext.class,0);
		}
		public IdStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idStatement; }
	}

	public final IdStatementContext idStatement() throws RecognitionException {
		IdStatementContext _localctx = new IdStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_idStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(ID);
			setState(132);
			idSuffix();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdSuffixContext extends ParserRuleContext {
		public TerminalNode ASSIGN() { return getToken(ArArduinoParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public IdSuffixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idSuffix; }
	}

	public final IdSuffixContext idSuffix() throws RecognitionException {
		IdSuffixContext _localctx = new IdSuffixContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_idSuffix);
		int _la;
		try {
			setState(141);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ASSIGN:
				enterOuterAlt(_localctx, 1);
				{
				setState(134);
				match(ASSIGN);
				setState(135);
				expression();
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				match(LPAREN);
				setState(138);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 103347781728L) != 0)) {
					{
					setState(137);
					args();
					}
				}

				setState(140);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(ArArduinoParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ArArduinoParser.ELSE, 0); }
		public IfStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStat; }
	}

	public final IfStatContext ifStat() throws RecognitionException {
		IfStatContext _localctx = new IfStatContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_ifStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(IF);
			setState(144);
			match(LPAREN);
			setState(145);
			expression();
			setState(146);
			match(RPAREN);
			setState(147);
			block();
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(148);
				match(ELSE);
				setState(149);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(ArArduinoParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStat; }
	}

	public final WhileStatContext whileStat() throws RecognitionException {
		WhileStatContext _localctx = new WhileStatContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_whileStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(WHILE);
			setState(153);
			match(LPAREN);
			setState(154);
			expression();
			setState(155);
			match(RPAREN);
			setState(156);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(ArArduinoParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStat; }
	}

	public final ReturnStatContext returnStat() throws RecognitionException {
		ReturnStatContext _localctx = new ReturnStatContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_returnStat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(RETURN);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 103347781728L) != 0)) {
				{
				setState(159);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMA() { return getTokens(ArArduinoParser.COMA); }
		public TerminalNode COMA(int i) {
			return getToken(ArArduinoParser.COMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			expression();
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMA) {
				{
				{
				setState(163);
				match(COMA);
				setState(164);
				expression();
				}
				}
				setState(169);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public OrExprContext orExpr() {
			return getRuleContext(OrExprContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			orExpr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrExprContext extends ParserRuleContext {
		public List<AndExprContext> andExpr() {
			return getRuleContexts(AndExprContext.class);
		}
		public AndExprContext andExpr(int i) {
			return getRuleContext(AndExprContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(ArArduinoParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(ArArduinoParser.OR, i);
		}
		public OrExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orExpr; }
	}

	public final OrExprContext orExpr() throws RecognitionException {
		OrExprContext _localctx = new OrExprContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_orExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			andExpr();
			setState(177);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(173);
				match(OR);
				setState(174);
				andExpr();
				}
				}
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndExprContext extends ParserRuleContext {
		public List<RelExprContext> relExpr() {
			return getRuleContexts(RelExprContext.class);
		}
		public RelExprContext relExpr(int i) {
			return getRuleContext(RelExprContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(ArArduinoParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(ArArduinoParser.AND, i);
		}
		public AndExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_andExpr; }
	}

	public final AndExprContext andExpr() throws RecognitionException {
		AndExprContext _localctx = new AndExprContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_andExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			relExpr();
			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(181);
				match(AND);
				setState(182);
				relExpr();
				}
				}
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelExprContext extends ParserRuleContext {
		public List<AddExprContext> addExpr() {
			return getRuleContexts(AddExprContext.class);
		}
		public AddExprContext addExpr(int i) {
			return getRuleContext(AddExprContext.class,i);
		}
		public List<RelOpContext> relOp() {
			return getRuleContexts(RelOpContext.class);
		}
		public RelOpContext relOp(int i) {
			return getRuleContext(RelOpContext.class,i);
		}
		public RelExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relExpr; }
	}

	public final RelExprContext relExpr() throws RecognitionException {
		RelExprContext _localctx = new RelExprContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_relExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			addExpr();
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 66060288L) != 0)) {
				{
				{
				setState(189);
				relOp();
				setState(190);
				addExpr();
				}
				}
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelOpContext extends ParserRuleContext {
		public TerminalNode GT() { return getToken(ArArduinoParser.GT, 0); }
		public TerminalNode LT() { return getToken(ArArduinoParser.LT, 0); }
		public TerminalNode LTE() { return getToken(ArArduinoParser.LTE, 0); }
		public TerminalNode GTE() { return getToken(ArArduinoParser.GTE, 0); }
		public TerminalNode EQ() { return getToken(ArArduinoParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(ArArduinoParser.NEQ, 0); }
		public RelOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relOp; }
	}

	public final RelOpContext relOp() throws RecognitionException {
		RelOpContext _localctx = new RelOpContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_relOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 66060288L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddExprContext extends ParserRuleContext {
		public List<MulExprContext> mulExpr() {
			return getRuleContexts(MulExprContext.class);
		}
		public MulExprContext mulExpr(int i) {
			return getRuleContext(MulExprContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(ArArduinoParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(ArArduinoParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(ArArduinoParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(ArArduinoParser.MINUS, i);
		}
		public AddExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addExpr; }
	}

	public final AddExprContext addExpr() throws RecognitionException {
		AddExprContext _localctx = new AddExprContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_addExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			mulExpr();
			setState(204);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(200);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(201);
				mulExpr();
				}
				}
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MulExprContext extends ParserRuleContext {
		public List<UnaryExprContext> unaryExpr() {
			return getRuleContexts(UnaryExprContext.class);
		}
		public UnaryExprContext unaryExpr(int i) {
			return getRuleContext(UnaryExprContext.class,i);
		}
		public List<TerminalNode> MUL() { return getTokens(ArArduinoParser.MUL); }
		public TerminalNode MUL(int i) {
			return getToken(ArArduinoParser.MUL, i);
		}
		public List<TerminalNode> DIV() { return getTokens(ArArduinoParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(ArArduinoParser.DIV, i);
		}
		public MulExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulExpr; }
	}

	public final MulExprContext mulExpr() throws RecognitionException {
		MulExprContext _localctx = new MulExprContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_mulExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			unaryExpr();
			setState(212);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MUL || _la==DIV) {
				{
				{
				setState(208);
				_la = _input.LA(1);
				if ( !(_la==MUL || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(209);
				unaryExpr();
				}
				}
				setState(214);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExprContext extends ParserRuleContext {
		public TerminalNode MINUS() { return getToken(ArArduinoParser.MINUS, 0); }
		public UnaryExprContext unaryExpr() {
			return getRuleContext(UnaryExprContext.class,0);
		}
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpr; }
	}

	public final UnaryExprContext unaryExpr() throws RecognitionException {
		UnaryExprContext _localctx = new UnaryExprContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_unaryExpr);
		try {
			setState(218);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				match(MINUS);
				setState(216);
				unaryExpr();
				}
				break;
			case TRUE:
			case FALSE:
			case LPAREN:
			case NUMBER:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(217);
				primary();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(ArArduinoParser.NUMBER, 0); }
		public TerminalNode TRUE() { return getToken(ArArduinoParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(ArArduinoParser.FALSE, 0); }
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(ArArduinoParser.ID, 0); }
		public PrimaryIdSuffixContext primaryIdSuffix() {
			return getRuleContext(PrimaryIdSuffixContext.class,0);
		}
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_primary);
		try {
			setState(229);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(220);
				match(NUMBER);
				}
				break;
			case TRUE:
				enterOuterAlt(_localctx, 2);
				{
				setState(221);
				match(TRUE);
				}
				break;
			case FALSE:
				enterOuterAlt(_localctx, 3);
				{
				setState(222);
				match(FALSE);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 4);
				{
				setState(223);
				match(LPAREN);
				setState(224);
				expression();
				setState(225);
				match(RPAREN);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 5);
				{
				setState(227);
				match(ID);
				setState(228);
				primaryIdSuffix();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryIdSuffixContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(ArArduinoParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ArArduinoParser.RPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public PrimaryIdSuffixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryIdSuffix; }
	}

	public final PrimaryIdSuffixContext primaryIdSuffix() throws RecognitionException {
		PrimaryIdSuffixContext _localctx = new PrimaryIdSuffixContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_primaryIdSuffix);
		int _la;
		try {
			setState(237);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(231);
				match(LPAREN);
				setState(233);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 103347781728L) != 0)) {
					{
					setState(232);
					args();
					}
				}

				setState(235);
				match(RPAREN);
				}
				break;
			case PLUS:
			case MINUS:
			case MUL:
			case DIV:
			case GTE:
			case LTE:
			case EQ:
			case NEQ:
			case GT:
			case LT:
			case OR:
			case AND:
			case RPAREN:
			case SEMI:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT_T() { return getToken(ArArduinoParser.INT_T, 0); }
		public TerminalNode FLOAT_T() { return getToken(ArArduinoParser.FLOAT_T, 0); }
		public TerminalNode VOID() { return getToken(ArArduinoParser.VOID, 0); }
		public TerminalNode BOOL() { return getToken(ArArduinoParser.BOOL, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17280L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u00f2\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0001\u0000\u0005\u00006\b\u0000\n\u0000\f\u0000"+
		"9\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"?\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004[\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004b\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005g\b\u0005\n\u0005\f\u0005"+
		"j\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0005\u0007r\b\u0007\n\u0007\f\u0007u\t\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\b\u0082\b\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\n\u008b\b\n\u0001\n\u0003\n\u008e\b\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000b\u0097\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0003\r\u00a1\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0005"+
		"\u000e\u00a6\b\u000e\n\u000e\f\u000e\u00a9\t\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00b0\b\u0010\n\u0010"+
		"\f\u0010\u00b3\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011"+
		"\u00b8\b\u0011\n\u0011\f\u0011\u00bb\t\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0005\u0012\u00c1\b\u0012\n\u0012\f\u0012\u00c4\t\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014"+
		"\u00cb\b\u0014\n\u0014\f\u0014\u00ce\t\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0005\u0015\u00d3\b\u0015\n\u0015\f\u0015\u00d6\t\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0003\u0016\u00db\b\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0003\u0017\u00e6\b\u0017\u0001\u0018\u0001\u0018\u0003\u0018"+
		"\u00ea\b\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u00ee\b\u0018\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0000\u0000\u001a\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"02\u0000\u0004\u0001\u0000\u0014\u0019\u0001\u0000\u0010\u0011\u0001\u0000"+
		"\u0012\u0013\u0002\u0000\u0007\t\u000e\u000e\u00f3\u00007\u0001\u0000"+
		"\u0000\u0000\u0002>\u0001\u0000\u0000\u0000\u0004@\u0001\u0000\u0000\u0000"+
		"\u0006H\u0001\u0000\u0000\u0000\ba\u0001\u0000\u0000\u0000\nc\u0001\u0000"+
		"\u0000\u0000\fk\u0001\u0000\u0000\u0000\u000eo\u0001\u0000\u0000\u0000"+
		"\u0010\u0081\u0001\u0000\u0000\u0000\u0012\u0083\u0001\u0000\u0000\u0000"+
		"\u0014\u008d\u0001\u0000\u0000\u0000\u0016\u008f\u0001\u0000\u0000\u0000"+
		"\u0018\u0098\u0001\u0000\u0000\u0000\u001a\u009e\u0001\u0000\u0000\u0000"+
		"\u001c\u00a2\u0001\u0000\u0000\u0000\u001e\u00aa\u0001\u0000\u0000\u0000"+
		" \u00ac\u0001\u0000\u0000\u0000\"\u00b4\u0001\u0000\u0000\u0000$\u00bc"+
		"\u0001\u0000\u0000\u0000&\u00c5\u0001\u0000\u0000\u0000(\u00c7\u0001\u0000"+
		"\u0000\u0000*\u00cf\u0001\u0000\u0000\u0000,\u00da\u0001\u0000\u0000\u0000"+
		".\u00e5\u0001\u0000\u0000\u00000\u00ed\u0001\u0000\u0000\u00002\u00ef"+
		"\u0001\u0000\u0000\u000046\u0003\u0002\u0001\u000054\u0001\u0000\u0000"+
		"\u000069\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000"+
		"\u0000\u00008:\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000:;\u0005"+
		"\u0000\u0000\u0001;\u0001\u0001\u0000\u0000\u0000<?\u0003\u0004\u0002"+
		"\u0000=?\u0003\u0006\u0003\u0000><\u0001\u0000\u0000\u0000>=\u0001\u0000"+
		"\u0000\u0000?\u0003\u0001\u0000\u0000\u0000@A\u0005\u0001\u0000\u0000"+
		"AB\u0005$\u0000\u0000BC\u0005 \u0000\u0000CD\u00032\u0019\u0000DE\u0005"+
		"\u000f\u0000\u0000EF\u0003\u001e\u000f\u0000FG\u0005!\u0000\u0000G\u0005"+
		"\u0001\u0000\u0000\u0000HI\u0005\n\u0000\u0000IJ\u0003\b\u0004\u0000J"+
		"\u0007\u0001\u0000\u0000\u0000KL\u0005\f\u0000\u0000LM\u0005\u001c\u0000"+
		"\u0000MN\u0005\u001d\u0000\u0000NO\u0005 \u0000\u0000OP\u0005\t\u0000"+
		"\u0000Pb\u0003\u000e\u0007\u0000QR\u0005\r\u0000\u0000RS\u0005\u001c\u0000"+
		"\u0000ST\u0005\u001d\u0000\u0000TU\u0005 \u0000\u0000UV\u0005\t\u0000"+
		"\u0000Vb\u0003\u000e\u0007\u0000WX\u0005$\u0000\u0000XZ\u0005\u001c\u0000"+
		"\u0000Y[\u0003\n\u0005\u0000ZY\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000"+
		"\u0000[\\\u0001\u0000\u0000\u0000\\]\u0005\u001d\u0000\u0000]^\u0005 "+
		"\u0000\u0000^_\u00032\u0019\u0000_`\u0003\u000e\u0007\u0000`b\u0001\u0000"+
		"\u0000\u0000aK\u0001\u0000\u0000\u0000aQ\u0001\u0000\u0000\u0000aW\u0001"+
		"\u0000\u0000\u0000b\t\u0001\u0000\u0000\u0000ch\u0003\f\u0006\u0000de"+
		"\u0005\"\u0000\u0000eg\u0003\f\u0006\u0000fd\u0001\u0000\u0000\u0000g"+
		"j\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000"+
		"\u0000i\u000b\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000kl\u0005"+
		"$\u0000\u0000lm\u0005 \u0000\u0000mn\u00032\u0019\u0000n\r\u0001\u0000"+
		"\u0000\u0000os\u0005\u001e\u0000\u0000pr\u0003\u0010\b\u0000qp\u0001\u0000"+
		"\u0000\u0000ru\u0001\u0000\u0000\u0000sq\u0001\u0000\u0000\u0000st\u0001"+
		"\u0000\u0000\u0000tv\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000"+
		"vw\u0005\u001f\u0000\u0000w\u000f\u0001\u0000\u0000\u0000x\u0082\u0003"+
		"\u0004\u0002\u0000yz\u0003\u0012\t\u0000z{\u0005!\u0000\u0000{\u0082\u0001"+
		"\u0000\u0000\u0000|\u0082\u0003\u0016\u000b\u0000}\u0082\u0003\u0018\f"+
		"\u0000~\u007f\u0003\u001a\r\u0000\u007f\u0080\u0005!\u0000\u0000\u0080"+
		"\u0082\u0001\u0000\u0000\u0000\u0081x\u0001\u0000\u0000\u0000\u0081y\u0001"+
		"\u0000\u0000\u0000\u0081|\u0001\u0000\u0000\u0000\u0081}\u0001\u0000\u0000"+
		"\u0000\u0081~\u0001\u0000\u0000\u0000\u0082\u0011\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0005$\u0000\u0000\u0084\u0085\u0003\u0014\n\u0000\u0085"+
		"\u0013\u0001\u0000\u0000\u0000\u0086\u0087\u0005\u000f\u0000\u0000\u0087"+
		"\u008e\u0003\u001e\u000f\u0000\u0088\u008a\u0005\u001c\u0000\u0000\u0089"+
		"\u008b\u0003\u001c\u000e\u0000\u008a\u0089\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c"+
		"\u008e\u0005\u001d\u0000\u0000\u008d\u0086\u0001\u0000\u0000\u0000\u008d"+
		"\u0088\u0001\u0000\u0000\u0000\u008e\u0015\u0001\u0000\u0000\u0000\u008f"+
		"\u0090\u0005\u0002\u0000\u0000\u0090\u0091\u0005\u001c\u0000\u0000\u0091"+
		"\u0092\u0003\u001e\u000f\u0000\u0092\u0093\u0005\u001d\u0000\u0000\u0093"+
		"\u0096\u0003\u000e\u0007\u0000\u0094\u0095\u0005\u0003\u0000\u0000\u0095"+
		"\u0097\u0003\u000e\u0007\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096"+
		"\u0097\u0001\u0000\u0000\u0000\u0097\u0017\u0001\u0000\u0000\u0000\u0098"+
		"\u0099\u0005\u0004\u0000\u0000\u0099\u009a\u0005\u001c\u0000\u0000\u009a"+
		"\u009b\u0003\u001e\u000f\u0000\u009b\u009c\u0005\u001d\u0000\u0000\u009c"+
		"\u009d\u0003\u000e\u0007\u0000\u009d\u0019\u0001\u0000\u0000\u0000\u009e"+
		"\u00a0\u0005\u000b\u0000\u0000\u009f\u00a1\u0003\u001e\u000f\u0000\u00a0"+
		"\u009f\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1"+
		"\u001b\u0001\u0000\u0000\u0000\u00a2\u00a7\u0003\u001e\u000f\u0000\u00a3"+
		"\u00a4\u0005\"\u0000\u0000\u00a4\u00a6\u0003\u001e\u000f\u0000\u00a5\u00a3"+
		"\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a5"+
		"\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u001d"+
		"\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00aa\u00ab"+
		"\u0003 \u0010\u0000\u00ab\u001f\u0001\u0000\u0000\u0000\u00ac\u00b1\u0003"+
		"\"\u0011\u0000\u00ad\u00ae\u0005\u001a\u0000\u0000\u00ae\u00b0\u0003\""+
		"\u0011\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00b0\u00b3\u0001\u0000"+
		"\u0000\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b1\u00b2\u0001\u0000"+
		"\u0000\u0000\u00b2!\u0001\u0000\u0000\u0000\u00b3\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b9\u0003$\u0012\u0000\u00b5\u00b6\u0005\u001b\u0000\u0000"+
		"\u00b6\u00b8\u0003$\u0012\u0000\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b8"+
		"\u00bb\u0001\u0000\u0000\u0000\u00b9\u00b7\u0001\u0000\u0000\u0000\u00b9"+
		"\u00ba\u0001\u0000\u0000\u0000\u00ba#\u0001\u0000\u0000\u0000\u00bb\u00b9"+
		"\u0001\u0000\u0000\u0000\u00bc\u00c2\u0003(\u0014\u0000\u00bd\u00be\u0003"+
		"&\u0013\u0000\u00be\u00bf\u0003(\u0014\u0000\u00bf\u00c1\u0001\u0000\u0000"+
		"\u0000\u00c0\u00bd\u0001\u0000\u0000\u0000\u00c1\u00c4\u0001\u0000\u0000"+
		"\u0000\u00c2\u00c0\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000"+
		"\u0000\u00c3%\u0001\u0000\u0000\u0000\u00c4\u00c2\u0001\u0000\u0000\u0000"+
		"\u00c5\u00c6\u0007\u0000\u0000\u0000\u00c6\'\u0001\u0000\u0000\u0000\u00c7"+
		"\u00cc\u0003*\u0015\u0000\u00c8\u00c9\u0007\u0001\u0000\u0000\u00c9\u00cb"+
		"\u0003*\u0015\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00cb\u00ce\u0001"+
		"\u0000\u0000\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001"+
		"\u0000\u0000\u0000\u00cd)\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001\u0000"+
		"\u0000\u0000\u00cf\u00d4\u0003,\u0016\u0000\u00d0\u00d1\u0007\u0002\u0000"+
		"\u0000\u00d1\u00d3\u0003,\u0016\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000"+
		"\u00d3\u00d6\u0001\u0000\u0000\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000"+
		"\u00d4\u00d5\u0001\u0000\u0000\u0000\u00d5+\u0001\u0000\u0000\u0000\u00d6"+
		"\u00d4\u0001\u0000\u0000\u0000\u00d7\u00d8\u0005\u0011\u0000\u0000\u00d8"+
		"\u00db\u0003,\u0016\u0000\u00d9\u00db\u0003.\u0017\u0000\u00da\u00d7\u0001"+
		"\u0000\u0000\u0000\u00da\u00d9\u0001\u0000\u0000\u0000\u00db-\u0001\u0000"+
		"\u0000\u0000\u00dc\u00e6\u0005#\u0000\u0000\u00dd\u00e6\u0005\u0005\u0000"+
		"\u0000\u00de\u00e6\u0005\u0006\u0000\u0000\u00df\u00e0\u0005\u001c\u0000"+
		"\u0000\u00e0\u00e1\u0003\u001e\u000f\u0000\u00e1\u00e2\u0005\u001d\u0000"+
		"\u0000\u00e2\u00e6\u0001\u0000\u0000\u0000\u00e3\u00e4\u0005$\u0000\u0000"+
		"\u00e4\u00e6\u00030\u0018\u0000\u00e5\u00dc\u0001\u0000\u0000\u0000\u00e5"+
		"\u00dd\u0001\u0000\u0000\u0000\u00e5\u00de\u0001\u0000\u0000\u0000\u00e5"+
		"\u00df\u0001\u0000\u0000\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e6"+
		"/\u0001\u0000\u0000\u0000\u00e7\u00e9\u0005\u001c\u0000\u0000\u00e8\u00ea"+
		"\u0003\u001c\u000e\u0000\u00e9\u00e8\u0001\u0000\u0000\u0000\u00e9\u00ea"+
		"\u0001\u0000\u0000\u0000\u00ea\u00eb\u0001\u0000\u0000\u0000\u00eb\u00ee"+
		"\u0005\u001d\u0000\u0000\u00ec\u00ee\u0001\u0000\u0000\u0000\u00ed\u00e7"+
		"\u0001\u0000\u0000\u0000\u00ed\u00ec\u0001\u0000\u0000\u0000\u00ee1\u0001"+
		"\u0000\u0000\u0000\u00ef\u00f0\u0007\u0003\u0000\u0000\u00f03\u0001\u0000"+
		"\u0000\u0000\u00157>Zahs\u0081\u008a\u008d\u0096\u00a0\u00a7\u00b1\u00b9"+
		"\u00c2\u00cc\u00d4\u00da\u00e5\u00e9\u00ed";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}